import asyncio
import os

import grpc
import meterusage_pb2
import meterusage_pb2_grpc

from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

load_dotenv()

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
    print(os.getenv("SERVER_ADDRESS"), " :ADDY")
    async with grpc.aio.insecure_channel(os.getenv("SERVER_ADDRESS")) as channel:
        stub = meterusage_pb2_grpc.MeterUsageServiceStub(channel)
        response = await stub.GetMeterUsage(meterusage_pb2.MeterUsageRequest())

    return {"data": [{"time": record.time, "meterusage": record.meterusage} for record in response.records]}


if __name__ == "__main__":
    import uvicorn
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8002)
