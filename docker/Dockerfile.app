FROM python:3.9-alpine

WORKDIR /app

COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN apk update && apk add build-base g++ linux-headers
RUN pip install --upgrade pip setuptools wheel

RUN pip install grpcio==1.64.1
RUN pip install grpcio-tools==1.62.1

# copy files
COPY ../grpc/client.py /app
COPY ../frontend /app/frontend
COPY ../grpc/meterusage_pb2.py /app
COPY ../grpc/meterusage_pb2_grpc.py /app

RUN pip install -r requirements.txt

EXPOSE 8081

# Startup command
CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]