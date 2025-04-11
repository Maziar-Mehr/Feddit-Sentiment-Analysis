# 🌟 Subfeddit – Sentiment Analysis Microservices 🚀  

## 🏆 **Overview**  
Welcome to **Subfeddit**, a high-performance **Flask-based Sentiment Analysis API** powered by **Hugging Face Transformers**. This microservice **dynamically analyzes user-generated comments**, classifying them as **positive** or **negative**, while providing a confidence score (`polarity`).  

🎯 **Key Features:**  
✅ Real-time **sentiment classification**  
✅ Optimized for **speed and scalability**  
✅ Seamless **integration with microservices**  
✅ Automated **testing via GitHub Actions**  

## 🏗️ **System Architecture**  

| Component                                  | Functionality                                                 |
|--------------------------------------------|--------------------------------------------------------------|
| 🚀 **API Gateway (Flask)**                 | Manages incoming requests, processes sentiment analysis, and integrates with external services. |
| 🤖 **Sentiment Analysis Module (SentenceTransformer)** | Classifies user comments as positive or negative and computes polarity scores using a lightweight NLP model. |
| 📜 **Logging & Analytics Foundation (PostgreSQL)** | Provides a structured foundation for tracking API interactions, debugging, and potential future analytics. |


**Architecture Flow:**  
1️⃣ **User submits a comment** → 📡 API Gateway processes request  
2️⃣ **API Gateway forwards it to NLP Model** → 🤖 Sentiment analysis occurs  
3️⃣ **Result is returned to the user** → 📜 Logging ensures request tracking  

## 🛠️ **Tech Stack**  

🔹 **Python** (Flask-based API)  
🔹 **Transformers** – Hugging Face NLP models  
🔹 **Docker** – Containerized deployment  
🔹 **GitHub Actions** – Automated testing  

Markdown

## 📦 Installation & Dependency Management  
Install the required dependencies using the following command:

```bash
make install

