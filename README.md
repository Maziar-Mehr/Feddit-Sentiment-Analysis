Subfeddit – Sentiment Analysis Microservices 🚀
Overview
Subfeddit is a Flask-based Sentiment Analysis API powered by Hugging Face Transformers. It dynamically analyzes user-generated comments, classifying them as positive or negative, and provides a polarity confidence score.

System Architecture 🏗️
🔹 API Gateway (Flask)
Handles user requests and performs sentiment analysis.

Provides RESTful endpoints for querying processed comments.

🔹 Sentiment Analysis Service (NLP Model)
Uses Hugging Face Transformers for text classification.

Outputs structured results with:

Polarity (confidence score)

Classification (positive or negative)

🔹 Logging Mechanism
Tracks API requests for debugging and performance monitoring.

Tech Stack 🛠️
✅ Python (Flask-based API) ✅ Transformers – Hugging Face NLP models ✅ Docker – Containerized deployment ✅ GitHub Actions – Automated testing and CI/CD
