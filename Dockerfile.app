FROM python:3.7-alpine

WORKDIR /app

COPY ./app.py /app
COPY ./frontend /app/frontend
COPY ./data /app/data
COPY ./meterusage_pb2.py /app
COPY ./meterusage_pb2_grpc.py /app

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8081

# Startup command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]