import pytest
import json
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Feddit API!" in response.data

def test_comments_valid(client):
    """Test fetching comments with a valid subfeddit_id"""
    response = client.get("/api/v1/comments?subfeddit_id=1&skip=0&limit=2")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert "polarity" in data[0]

def test_comments_invalid(client):
    """Test invalid requests"""
    response = client.get("/api/v1/comments?skip=0&limit=2")
    assert response.status_code == 400
    assert b"Missing required parameter: subfeddit_id" in response.data
