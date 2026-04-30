# 📱 SMS Scam Detection System

An AI-powered full-stack application that analyzes SMS messages and detects potential scams using Natural Language Processing.

---

## 🚀 Project Overview

This project is designed to simulate a real-world cybersecurity tool that helps users identify suspicious SMS messages. It uses a backend API and will integrate AI models to classify messages as:

* Likely Scam
* Likely Legitimate
* Uncertain

---

## 🧱 Project Structure

```
SMS_Scam_Detection/
├── backend/
│   └── app/
│       ├── routes/        # API endpoints
│       └── services/      # Business logic & AI integration
│
├── frontend/              # React UI (to be implemented)
├── docs/                  # Architecture & design documentation
├── screenshots/           # UI images for README
├── dataset/               # Sample SMS data for testing
```

---

## 🧠 Architecture

* **Backend:** FastAPI (Python)
* **Frontend:** React.js (planned)
* **AI Integration:** Hugging Face (planned)


---

## ⚙️ Setup Instructions

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

### 3. Run Backend Server

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Environment Variables

Create a `.env` file in the backend folder:

```
HUGGINGFACE_API_KEY=your_api_key_here
```

⚠️ Do NOT push `.env` to GitHub.

---

## 🧪 Current Status

* [x] Project structure created
* [ ] FastAPI backend setup
* [ ] API endpoint creation
* [ ] AI integration
* [ ] Frontend development
* [ ] Deployment

---

## 🎯 Learning Objectives

* Build full-stack AI applications
* Understand API design and backend architecture
* Integrate AI models using Hugging Face
* Deploy production-ready applications

---

## 📌 Notes

This project is being built step-by-step with a focus on understanding every component rather than copying code.

---

## 👩‍💻 Author

Javeria Samreen

