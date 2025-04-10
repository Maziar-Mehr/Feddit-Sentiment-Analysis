# 🌟 Subfeddit – Sentiment Analysis Microservices 🚀  

## 🏆 **Overview**  
Welcome to **Subfeddit**, a high-performance **Flask-based Sentiment Analysis API** powered by **Hugging Face Transformers**. This microservice **dynamically analyzes user-generated comments**, classifying them as **positive** or **negative**, while providing a confidence score (`polarity`).  

🎯 **Key Features:**  
✅ Real-time **sentiment classification**  
✅ Optimized for **speed and scalability**  
✅ Seamless **integration with microservices**  
✅ Automated **testing via GitHub Actions**  

## 🏗️ **System Architecture**  

| Component                 | Functionality                                         |
|---------------------------|------------------------------------------------------|
| 🚀 **API Gateway (Flask)** | Handles user requests & routes them to analysis    |
| 🤖 **NLP Model (HuggingFace)** | Classifies sentiment & provides confidence scores  |
| 📜 **Logging Mechanism**  | Tracks API interactions & enables debugging         |

**Architecture Flow:**  
1️⃣ **User submits a comment** → 📡 API Gateway processes request  
2️⃣ **API Gateway forwards it to NLP Model** → 🤖 Sentiment analysis occurs  
3️⃣ **Result is returned to the user** → 📜 Logging ensures request tracking  

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
