import requests
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sentence_transformers import SentenceTransformer

# ✅ Initialize lightweight sentiment analysis model
try:
    sentiment_analyzer = SentenceTransformer("paraphrase-MiniLM-L6-v2")  # Small, efficient model
except Exception as e:
    print(f"⚠️ Sentiment analysis model failed to load: {str(e)}")
    sentiment_analyzer = None

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@db:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Initialize SQLAlchemy
db = SQLAlchemy(app)

# ✅ Feddit API Base URL
FEDDIT_API_URL = "http://127.0.0.1:8080/api/v1/comments"

# ✅ Default route to prevent 404 errors
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Feddit API!"})

# ✅ API endpoint for fetching comments with sentiment analysis
@app.route('/api/v1/comments', methods=['GET'])
def get_comments():
    try:
        # ✅ Get required parameters
        subfeddit_id = request.args.get('subfeddit_id', type=int)
        skip = request.args.get('skip', 0, type=int)
        limit = request.args.get('limit', 10, type=int)

        # ✅ Validate subfeddit_id
        if subfeddit_id is None:
            return jsonify({"error": "⚠️ Missing required parameter: subfeddit_id"})

        # ✅ Fetch comments from Feddit
        response = requests.get(f"{FEDDIT_API_URL}/?subfeddit_id={subfeddit_id}&skip={skip}&limit={limit}")
        response.raise_for_status()  # Catch API errors

        comments = response.json()

        # ✅ Process comments with sentiment analysis
        results = []
        for comment in comments.get("comments", []):
            if "text" in comment:
                try:
                    if sentiment_analyzer:
                        embedding = sentiment_analyzer.encode(comment["text"])
                        polarity = float(embedding.mean())  # Simple polarity calculation
                        classification = "positive" if polarity > 0 else "negative"
                        results.append({
                            "id": comment.get("id"),
                            "username": comment.get("username", "Unknown"),
                            "text": comment["text"],
                            "created_at": comment.get("created_at"),
                            "polarity": polarity,
                            "classification": classification
                        })
                    else:
                        results.append({
                            "id": comment.get("id"),
                            "username": comment.get("username", "Unknown"),
                            "text": comment["text"],
                            "created_at": comment.get("created_at"),
                            "error": "⚠️ Sentiment analysis unavailable"
                        })
                except Exception as sentiment_error:
                    results.append({"error": f"Sentiment analysis failed: {str(sentiment_error)}"})
            else:
                results.append({"error": "⚠️ Invalid comment format", "content": str(comment)})

        return jsonify(results)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"⚠️ Failed to fetch comments: {str(e)}"})

# ✅ Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
