import pytest
import json
from unittest.mock import patch
from main import app

@pytest.fixture
def client():
    """
    Creates a test client for the Flask app.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """
    Test the home route.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to Feddit API!"

@patch("requests.get")
def test_comments_valid(mock_get, client):
    """
    Test fetching comments with a valid subfeddit_id while the external API is mocked.
    
    Here we ensure that the external API (mocked) returns the proper dictionary format,
    and that the route processes it to produce a list of comment objects.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "comments": [
            {"id": 1, "username": "user_0", "text": "It looks great!", "created_at": 1622847172, "polarity": 0.005987, "classification": "positive"},
            {"id": 2, "username": "user_1", "text": "Love it.", "created_at": 1622850772, "polarity": 0.007155, "classification": "positive"},
            {"id": 3, "username": "user_2", "text": "Awesome.", "created_at": 1622854372, "polarity": 0.006182, "classification": "positive"},
            {"id": 4, "username": "user_3", "text": "Well done!", "created_at": 1622857972, "polarity": 0.001269, "classification": "positive"},
            {"id": 5, "username": "user_4", "text": "Looks decent.", "created_at": 1622861572, "polarity": 0.005608, "classification": "positive"}
        ]
    }

    response = client.get("/api/v1/comments?subfeddit_id=1&skip=0&limit=5")
    assert response.status_code == 200
    data = json.loads(response.data)

    # Ensure we receive a list of processed comment items.
    assert isinstance(data, list)
    assert len(data) == 5
    assert all("classification" in comment and comment["classification"] == "positive" for comment in data)
