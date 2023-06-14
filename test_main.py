import pytest

from farm.main import app



@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, world farm2!"