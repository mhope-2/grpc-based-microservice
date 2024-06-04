import grpc
import meterusage_pb2
import meterusage_pb2_grpc

from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI


app = FastAPI(title="an HTTP server that serves data from a gRPC server as JSON")

# Serve the frontend as a static file
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/meter/usage/")
async def read_meter_usage():
    """
    Returns the data served by the gRPC server as JSON
    :return:
    """
    # TODO: move to env variable
    with grpc.insecure_channel("grpc_server:50051") as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(meterusage_pb2.MeterUsageRequest())

    return {"data": [{"time": record.time, "meterusage": record.meterusage} for record in response.records]}

