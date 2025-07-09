# Smart Waste Scanner

Smart Waste Scanner is a cross-platform eco-sustainability app that helps users identify and classify waste using AI. The app supports typing, scanning, or uploading an image to detect waste type, and provides eco-friendly disposal tips and creative reuse suggestions. It includes user authentication, dashboard history, and gamification to track your environmental impact.

---

## Features

Identify waste items via:
- Text input
- Image upload
- Camera scan (mobile & webcam)

 AI-powered suggestions:
- Waste category detection (e.g., plastic, metal, paper)
- Eco-friendly disposal tips
- Reuse ideas for common waste

User system:
- Firebase login/signup with email verification
- Auth-protected routes

Progress tracking:
- Dashboard with history of scanned items
- Gamification badges and eco-points

Works on mobile & web
- Offline-ready (PWA support)
- Android/iOS compatible

Tech Stack:
- **Frontend**: React + Axios + Webcam integration
- **Backend**: Flask + Flask-CORS + Pillow (image support)
- **Auth**: Firebase Email/Password authentication

---

## Getting Started

### Prerequisites
- Node.js + npm
- Python 3.9+
- Firebase project with Email/Password enabled

### 🔧 Local Setup

#### 1. Backend (Flask)
```bash
cd server
pip install -r requirements.txt
python app.py
```

#### 2. Frontend (React)
```bash
cd client
npm install
npm start
```

---

## Firebase Config Example
Add your Firebase credentials in `client/src/firebase.js`:
```js
const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
  storageBucket: "...",
  messagingSenderId: "...",
  appId: "..."
};
```

---

## Folder Structure
```
smart_waste_scanner/
├── client/       # React frontend
├── server/       # Flask backend
├── data/         # Datasets if needed later
└── README.md
```


