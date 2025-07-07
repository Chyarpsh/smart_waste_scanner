# 🌿 Smart Eco Scanner

> **Smart Eco Scanner** is an AI-powered full-stack web app that helps users classify waste items (e.g., coffee cups, plastic bags, batteries) into recyclable, compostable, or trash — while offering sustainability tips and tracking eco habits.

Built using **React**, **Flask**, and **Firebase**, this project showcases end-to-end skills across **AI logic, cloud integration, frontend/backend development, and real deployment** — making it ideal for real-world use and job applications.

---

## 🌟 Features

✅ Classifies items using smart AI or rule-based logic  
✅ Accepts voice input for hands-free classification  
✅ Provides real-time eco-friendly disposal tips  
✅ Tracks user actions & environmental impact in cloud  
✅ Supports user authentication with Firebase  
✅ Dashboard for usage analytics and eco stats  
✅ Fully deployable with React (Vercel) + Flask (Render)

---

## 🛠 Tech Stack

| Layer         | Tools Used                          |
|---------------|-------------------------------------|
| **Frontend**  | React, Tailwind CSS                 |
| **Backend**   | Flask (Python), REST API            |
| **AI Logic**  | Rule-based logic / OpenAI API       |
| **Database**  | Firebase Firestore (cloud-hosted)   |
| **Auth**      | Firebase Authentication             |
| **Voice Input** | Web Speech API (React)             |
| **Dashboard** | Chart.js or Recharts (React)        |
| **Deployment**| Vercel (client) + Render (server)   |

---

## 📁 Project Structure

```
smart_eco_scanner/
├── client/       # React frontend
├── server/       # Flask backend
├── data/         # Item rules, logs (CSV)
└── README.md
```

---

## 🚀 Getting Started (Local Dev)

### 🔧 Backend (Flask)

```bash
cd server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install flask
python app.py
```

### 🌐 Frontend (React)

```bash
cd client
npm install
npm start
```

App will run at `http://localhost:3000`, connected to Flask API on `http://localhost:5000`.

---

## 🔐 Firebase (Required for Full Features)

- Firebase Auth: for secure user login
- Firestore DB: to save item history per user

You'll need a Firebase project, API key, and `.env` file in both client/server. Setup steps will be provided in `/firebase/README.md`.

---

## 📊 Included Features

- Voice input for hands-free waste classification
- Dashboard with weekly impact stats per user
- Firebase user accounts and personal logs
- Cloud-deployed app ready to share publicly

---

## 💼 Why This Project Matters

Smart Eco Scanner was built as a portfolio-ready capstone to demonstrate:
- End-to-end software development
- AI application without external dataset dependency
- Cloud integration and secure deployment
- Job-role alignment with Cloud, QA, AI, and full-stack positions

---
