# 📝 NoteCloud – Firebase-Powered Cloud Notes App

NoteCloud is a secure, minimal, and fast **note-taking web app** built with **Flask** and **Firebase**.  
It supports **user authentication**, **cloud sync**, and allows users to **add, view, and delete notes from anywhere**.

---

## 🚀 Features

- 🔐 Email + Password Login (Firebase Auth)
- ☁️ Realtime Cloud Sync (Firebase Realtime DB)
- 🧠 Add, View & Delete Notes (per user)
- 🌐 Flask + Pyrebase Integration
- 💾 Hosted on [Render](https://render.com/)
- 🎨 Responsive UI with Tailwind CSS

---

## 🖼️ Screenshots

> *(Add your screenshots in the `/screenshots` folder and link here)*

| Login Page | Dashboard |
|------------|-----------|
| ![Login](screenshots/login.png) | ![Dashboard](screenshots/dashboard.png) |

---

## 🔧 Tech Stack

| Layer        | Tech Used                        |
|--------------|----------------------------------|
| Frontend     | HTML, Tailwind CSS               |
| Backend      | Python (Flask)                   |
| Auth         | Firebase Authentication          |
| Database     | Firebase Realtime Database       |
| Hosting      | Render                           |

---

## 💻 Installation

```bash
git clone https://github.com/your-username/notecloud.git
cd notecloud
pip install -r requirements.txt
Create a file named firebase_config.json in the root directory with your Firebase config:

json
Copy
Edit
{
  "apiKey": "YOUR_KEY",
  "authDomain": "YOUR_DOMAIN",
  "databaseURL": "YOUR_DB_URL",
  "projectId": "YOUR_PROJECT_ID",
  "storageBucket": "YOUR_BUCKET",
  "messagingSenderId": "YOUR_SENDER_ID",
  "appId": "YOUR_APP_ID"
}
🧪 Run the App Locally
bash
Copy
Edit
flask run
Visit: http://localhost:5000

☁️ Deploy on Render
Push code to GitHub

Create a render.yaml file:

yaml
Copy
Edit
services:
  - type: web
    name: notecloud
    env: python
    buildCommand: ""
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
Go to Render

Click New Web Service → Connect GitHub → Select repo

Add firebase_config.json in Render → Environment → Secret Files

Click Deploy

🙋‍♂️ Author
Sharan S
2nd Year Software Engineering @ Deakin University
🌐 GitHub

