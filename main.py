import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline

# Initialize sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

# Initialize Flask app
app = Flask(__name__)

# Database configuration (still needed for other purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy (for any additional local storage needs)
db = SQLAlchemy(app)

# Feddit API URL
FEDDIT_API_URL = "http://localhost:8080/api/v1/comments"

@app.route('/api/v1/comments/<subfeddit>', methods=['GET'])
def get_comments(subfeddit):
    try:
        # Fetch comments **directly from Feddit**
        response = requests.get(f"{FEDDIT_API_URL}/{subfeddit}")
        response.raise_for_status()  # Ensure we catch API errors
        comments = response.json()

        # Process comments with sentiment analysis
        results = [
            {
                "id": comment["id"],
                "username": comment["username"],
                "text": comment["text"],
                "created_at": comment["created_at"],
                "polarity": sentiment_analyzer(comment["text"])[0]["score"],  # Polarity score
                "classification": sentiment_analyzer(comment["text"])[0]["label"].lower()  # Positive or negative
            }
            for comment in comments
        ]
        return jsonify(results)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
