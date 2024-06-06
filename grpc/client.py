import os

import grpc
from meterusage_pb2 import MeterUsageRequest
from meterusage_pb2_grpc import MeterUsageServiceStub

from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

load_dotenv()

app = FastAPI(title="an HTTP server that serves data from a gRPC server as JSON")

# Serve the frontend as a static file
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

@app.get("/meter/usage/")
async def read_meter_usage():
    """
    Returns the data served by the gRPC server as JSON
    :return:
    """
    with grpc.insecure_channel(os.getenv("SERVER_ADDRESS")) as channel:
        stub = MeterUsageServiceStub(channel)
        response = stub.GetMeterUsage(MeterUsageRequest())

    return {"data": [{"time": record.time, "meterusage": record.meterusage} for record in response.records]}

