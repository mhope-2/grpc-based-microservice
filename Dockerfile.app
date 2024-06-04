FROM python:3.9-alpine

WORKDIR /app

# copy files
COPY ./app.py /app
COPY ./frontend /app/frontend
COPY ./meterusage_pb2.py /app
COPY ./meterusage_pb2_grpc.py /app

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN apk update && apk add --no-cache build-base gcc g++ linux-headers
RUN pip install --upgrade pip setuptools wheel

RUN pip install grpcio==1.64.1
RUN pip install grpcio-tools==1.62.1

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

# Startup command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]