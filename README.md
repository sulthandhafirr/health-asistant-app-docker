# Health Assistant App with Docker

## 📌 Project Overview

The **Health Assistant App** is a simple full-stack web application designed to help users monitor their health. It features:

* 🧮 BMI (Body Mass Index) Calculator
* 🔥 Daily Calorie Recommendation
* 🥗 Diet Suggestion
* 🧑‍⚕️ Health Check based on age and weight
* 🏃 Exercise Recommendations

The application is containerized using **Docker** for ease of deployment and reproducibility. It consists of:

* **Frontend**: Static HTML, CSS, and JavaScript, served by Nginx
* **Backend**: Python Flask API

---

## 🧱 Project Structure

```
health-assistant-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── Dockerfile
└── docker-compose.yml
```

---

## 🛠️ Step-by-Step Deployment with Docker

### 1. Clone the Repository

```
git clone https://github.com/sulthandhafirr/health-assistant-app.git
cd health-assistant-app
```

### 2. Build and Run Using Docker Compose

```
docker-compose up --build
```

This command will:

* Build the Flask backend
* Build the Nginx frontend
* Run both containers in the same Docker network

### 3. Open the App

Open your browser and go to:

```
http://localhost:8080
```

You will see the Health Assistant App homepage.

---

## 🔧 Docker Files

### Backend Dockerfile (`backend/Dockerfile`)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Frontend Dockerfile (`frontend/Dockerfile`)

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
```

### Docker Compose File (`docker-compose.yml`)

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"

  frontend:
    build: ./frontend
    ports:
      - "8080:80"
```

---

## 📷 Screenshots

### 1. BMI Calculator UI

![BMI Calculator](screenshots/bmi-calculator.png)

### 2. Docker Compose Running

![Docker Running](screenshots/docker-running.png)

---

## 🔗 GitHub Repository

Link: [https://github.com/sulthandhafirr/health-assistant-app](https://github.com/sulthandhafirr/health-assistant-app)

---

## ✅ Conclusion

This project demonstrates a simple full-stack health assistant app using Docker containers. It's lightweight, modular, and easy to extend with more health-related features.

You can now continue development, scale it with a database, or deploy it to cloud platforms like Heroku, Vercel, or Railway.
