# 📱 SMS Scam Detection System (AI-Powered)

An end-to-end **AI-powered web application** that detects scam SMS messages using Large Language Models (LLMs).
Built with a full-stack architecture and deployed for real-world usage.

---

## 🚀 Live Demo

 **Frontend (Vercel):** https://your-vercel-url.vercel.app
 **Backend (Render):** https://sms-scam-detection-app.onrender.com
 **API Docs:** https://sms-scam-detection-app.onrender.com/docs

---

## 🧠 Project Overview

This system analyzes SMS messages and classifies them into:

* **Likely Scam**
* **Likely Legitimate**
* **Uncertain**

It uses **prompt engineering + LLM inference** to detect:

* Urgency or pressure language
* Suspicious links
* Requests for money / OTP / personal data
* Impersonation of trusted organizations

---

## 🧱 Architecture

```
React Frontend (Vercel)
        ↓
FastAPI Backend (Render)
        ↓
Hugging Face LLM API
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI (Python)
* Pydantic
* Hugging Face Inference API
* Python-dotenv

### Frontend

* React.js
* Axios / Fetch API
* Custom UI styling

### Deployment

* Render (Backend)
* Vercel (Frontend)

---

## ✨ Features

*  AI-powered SMS scam detection
*  Prompt-engineered structured outputs
*  Confidence scoring
*  Fallback logic for reliability
*  Real-time API response
*  Modern responsive UI
*  Fully deployed full-stack system

---

## 🧪 Example

### Input

```
Your bank account will be blocked. Click now http://fakebank.com
```

### Output

```
Decision: Likely Scam  
Confidence: High  
Reason: Contains urgency, suspicious link, and impersonation
```

---

## ⚙️ Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/Jsamreen/Gen_AI_projects.git
cd Gen_AI_projects/apps/SMS_Scam_Detection
```

---

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Run Backend

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 4. Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🔐 Environment Variables

Create `.env` in backend:

```
HUGGINGFACE_API_KEY=your_api_key_here
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct
```

⚠️ Never commit `.env` to GitHub

---

## 📌 Key Implementation Details

* Designed **structured prompts** for consistent AI output
* Implemented **response parsing logic**
* Added **fallback handling** for API failures
* Managed **CORS configuration** for deployment
* Built **REST API architecture using FastAPI**

---

## 🎯 Learning Outcomes

* Full-stack AI application development
* API design & backend architecture
* LLM integration via Hugging Face
* Deployment using modern platforms
* Production-level debugging and error handling

---

## 👩‍💻 Author

**Javeria Samreen**
Melbourne, Australia

---

## ⭐ Future Improvements

* Chat-style conversational UI
* SMS dataset evaluation & accuracy metrics
* User authentication
* Logging & analytics dashboard
* Multi-language scam detection

---
