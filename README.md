# 🏥 ESP32 Smart Patient Monitoring System API

This is a simple REST API built with Flask and SQLite for an ESP32-based patient monitoring system.

The ESP32 device will:
- Read patient temperature
- Send/receive patient data via HTTP
- Display information on an OLED screen

---

## 🚀 Features

- Get patient information by code
- Add new patients to the database
- SQLite database storage
- JSON REST API
- Ready for ESP32 integration

---

## 🏗️ Project Structure
```text
patient_api/
│
├── app.py # Flask API
├── create_db.py # Database setup script
├── patients.db # SQLite database
├── requirements.txt
└── README.md
```
---

---

## ⚙️ Installation

### 1. Clone or download the project
```bash
git clone <your-repo>
cd patient_api
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
## 🗄️ Create Database
```bash 
python create_db.py
```
## ▶️ Run the API
``` bash
python app.py
```
Server runs at: http://127.0.0.1:5000

## 📡 API Endpoints
🔹 Get patient by code
GET /patient/<code>
Example:
GET http://127.0.0.1:5000/patient/1001
Response:
{
  "code": "1001",
  "name": "John Smith",
  "illness": "Diabetes",
  "medication": "Insulin",
  "schedule": "08:00",
  "notes": "Stable"
}

## 🧠 Tech Stack
- Python
- Flask
- SQLite
- JSON API
- ESP32 (client side)

## 🎯 Goal

Build a simple IoT healthcare system that connects an ESP32 device to a patient database via REST API.

