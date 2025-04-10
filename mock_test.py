import pytest
import json
from unittest.mock import patch
from main import app

@pytest.fixture
def client():
    """Creates a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to Feddit API!"

@patch("requests.get")
@patch("sentence_transformers.SentenceTransformer.encode")
def test_comments_valid(mock_encode, mock_get, client):
    """Test fetching comments with a valid subfeddit_id without calling real API"""
    
    # Mock API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "comments": [
            {"id": 1, "username": "user1", "text": "Great day!", "created_at": "2025-04-10T10:00:00"},
            {"id": 2, "username": "user2", "text": "Feeling sad.", "created_at": "2025-04-10T11:00:00"}
        ]
    }

    # Mock sentiment analysis output (forcing expected polarity values)
    mock_encode.side_effect = [
        [0.9] * 10,  # Strong positive
        [-0.7] * 10  # Strong negative
    ]

    response = client.get("/api/v1/comments?subfeddit_id=1&skip=0&limit=2")
    assert response.status_code == 200
    data = json.loads(response.data)

    assert isinstance(data, list)
    assert all("polarity" in item and "classification" in item for item in data)

    # Ensure classifications include at least one positive and one negative result
    classifications = [item["classification"] for item in data]
    assert "positive" in classifications
    assert "negative" in classifications

@patch("requests.get")
def test_comments_api_failure(mock_get, client):
    """Simulate external API failure to avoid real API calls"""
    mock_get.side_effect = Exception("API unavailable")

    response = client.get("/api/v1/comments?subfeddit_id=1&skip=0&limit=2")
    assert response.status_code == 200  # Adjust if error handling should return 500
    error_data = response.json
    assert "⚠️ Failed to fetch comments" in error_data["error"]
