from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline

# Initialize the Hugging Face sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for your database table
class TestTable(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)  # Ensure 'username' matches the 'comments' table schema
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# Endpoint to check API version
@app.route('/api/v1/version', methods=['GET'])
def get_version():
    return jsonify({"version": "1.0", "status": "Feddit API is running!"})

# Endpoint to fetch comments with sentiment analysis
@app.route('/api/v1/comments/<subfeddit>', methods=['GET'])
def get_comments(subfeddit):
    # Query the database using the correct column 'username'
    comments = TestTable.query.filter(TestTable.username.ilike(f"%{subfeddit}%")).limit(25).all()
    results = [
        {
            "id": comment.id,
            "username": comment.username,
            "text": comment.text,
            "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "polarity": sentiment_analyzer(comment.text)[0]["score"],  # Polarity score from Hugging Face
            "classification": sentiment_analyzer(comment.text)[0]["label"].lower()  # Positive or negative
        }
        for comment in comments
    ]
    return jsonify(results)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
