from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_users():
    response = client.get("/users")
    assert response.status_code == 200
