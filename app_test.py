from unittest.mock import patch, Mock
import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_read_meter_usage():
    # Mock the gRPC server response
    mock_response = Mock()
    mock_record_1 = Mock(time="2021-01-01T00:00:00", meterusage=58.9)
    mock_record_2 = Mock(time="2021-01-01T01:00:00", meterusage=56.0)
    mock_response.records = [mock_record_1, mock_record_2]

    # Patch the gRPC client stub to return the mock response
    with patch('app.meterusage_pb2_grpc.MeterUsageServiceStub') as mock_stub:
        mock_stub.return_value.GetMeterUsage.return_value = mock_response

        response = client.get("/meter/usage/")

    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {"time": "2021-01-01T00:00:00", "meterusage": 58.9},
            {"time": "2021-01-01T01:00:00", "meterusage": 56.0},
        ]
    }