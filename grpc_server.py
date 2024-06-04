import aiofiles
import asyncio
import logging

import csv
import grpc
import logging
import math

from concurrent import futures

import meterusage_pb2
import meterusage_pb2_grpc

logger = logging.getLogger(__name__)


class MeterUsageService(meterusage_pb2_grpc.MeterUsageServiceServicer):
    async def GetMeterUsage(self, request, context):
        """
        Opens and serves the data in the csv file as defined in MeterUsageResponse in the proto file
        :return:
        """
        records = []

        try:
            async with aiofiles.open('data/meterusage.csv', mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # handle NaN records by filling in with 0.0
                    if math.isnan(float(row["meterusage"])):
                        records.append(meterusage_pb2.MeterUsageRecord(time=row["time"], meterusage=0.0))
                    else:
                        records.append(
                            meterusage_pb2.MeterUsageRecord(time=row["time"], meterusage=float(row["meterusage"]))
                        )
        except Exception as exc:
            logger.exception(f"Error processing file or file contents; msg={exc}")

        return meterusage_pb2.MeterUsageResponse(records=records)

async def serve():
    server = grpc.aio.server() #grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterusage_pb2_grpc.add_MeterUsageServiceServicer_to_server(MeterUsageService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
