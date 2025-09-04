import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    payload = {
        "username": "testuser1",
        "email": "testuser1@example.com",
        "password": "strongpassword",
        "date": "2024-01-01",
        "gender": "male"
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code in [200, 400]

def test_login_user():
    payload = {
        "email": "testuser1@example.com",
        "password": "strongpassword"
    }
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "token_type" in data
