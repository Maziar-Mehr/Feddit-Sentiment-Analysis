# subfeddit
# Sentiment Analysis Microservices 🚀  

## **Overview**  
This repository hosts a **Microservices-based Sentiment Analysis API**, built with **Flask, Hugging Face Transformers, and PostgreSQL**. It provides an efficient way to analyze user-generated comments and classify them as **positive** or **negative** with confidence scores.

---

## **System Architecture 🏗️**  

Our microservices architecture consists of the following services:

### 🔹 **API Gateway (Flask)**
- Handles user requests and routes them to the appropriate service.  

### 🔹 **Sentiment Analysis Service (NLP Model)**
- Uses **RoBERTa-based Transformers** for text classification.  
- Runs **asynchronously** for fast inference.  

### 🔹 **Database Service (PostgreSQL)**
- Stores processed comments and sentiment scores.  
- Supports efficient retrieval for analytics.  

### 🔹 **Authentication & Logging Service**
- Implements **OAuth2** authentication.  
- Logs API interactions for monitoring and debugging.  

---

## **Tech Stack 🛠️**  

✅ **Python 3.11** (with virtual environment)  
✅ **Flask** – Lightweight API framework  
✅ **Transformers** – Hugging Face NLP models  
✅ **PostgreSQL** – Database for comment storage  
✅ **Docker** – Containerized microservices deployment  
✅ **Kubernetes** – For scalable orchestration  

---

## **Installation & Setup**  

### **Step 1: Clone the Repository**
```bash
git clone <your-repo-url>
cd sentiment-analysis-microservices
