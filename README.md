# 🌟 Subfeddit – Sentiment Analysis Microservices 🚀  

## 🏆 **Overview**  
Welcome to **Subfeddit**, a high-performance **Flask-based Sentiment Analysis API** powered by **Hugging Face Transformers**. This microservice **dynamically analyzes user-generated comments**, classifying them as **positive** or **negative**, while providing a confidence score (`polarity`).  

🎯 **Key Features:**  
✅ Real-time **sentiment classification**  
✅ Optimized for **speed and scalability**  
✅ Seamless **integration with microservices**  
✅ Automated **testing via GitHub Actions**  

## 🏗️ **System Architecture**  

┌──────────────────────────────┐ │ 🚀 API Gateway (Flask) │ │ - Handles user requests │ │ - Routes to sentiment model │ └──────────────┬───────────────┘ │ ┌──────────────▼──────────────┐ │ 🤖 NLP Model (HuggingFace) │ │ - Classifies sentiment │ │ - Outputs confidence scores │ └──────────────┬──────────────┘ │ ┌──────────────▼──────────────┐ │ 📜 Logging Mechanism │ │ - Tracks API interactions │ │ - Debugging & monitoring │ └─────────────────────────────┘

## 🛠️ **Tech Stack**  
🚀 **Built with cutting-edge technology!**  

🔹 **Python** (Flask-based API)  
🔹 **Transformers** – Hugging Face NLP models  
🔹 **Docker** – Containerized deployment  
🔹 **GitHub Actions** – Automated testing  

## 🚀 **Installation & Setup**  

### 📥 **1️⃣ Clone the Repository**
```bash
git clone <your-repo-url>
cd subfeddit
