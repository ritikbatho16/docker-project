 Docker Microservices Project

Overview
This project demonstrates a microservices architecture using Docker and Docker Compose. It consists of two services:

- 🟢 Flask Microservice (Python) – Provides REST APIs  
- 🔵 Node.js Application (Express) – Consumes Flask APIs  

Both services are containerized and run together using Docker Compose.

---

Project Structure

dockerproject/
│── docker-compose.yml
│
├── flask-microservice/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── node-docker-app/
    ├── package.json
    ├── server.js
    └── Dockerfile


How to Run

Clone the repository:
git clone https://github.com/ritikbatho16/docker-project.git
cd docker-project

Run the project:
docker compose up --build

Services

Node.js App:
http://localhost:3000

Flask API:
http://localhost:5000/user  
http://localhost:5000/product  

---

Microservice Communication

Node.js service calls Flask API using Docker internal networking:

http://flask-app:5000/user

Note: Inside Docker, service names are used instead of localhost.

---

Screenshots

Flask API Response
https://github.com/ritikbatho16/docker-project/blob/main/flaskapi.png

Node.js Response
![Node API](screenshots/node.png)

---

Tech Stack

- Docker  
- Docker Compose  
- Node.js (Express)  
- Python (Flask)  

---

Features

- Multi-container setup  
- Microservices architecture  
- Inter-service communication  
- REST APIs  
- Easy setup with Docker  

---

Future Improvements

- Add MongoDB or PostgreSQL  
- Use Nginx for reverse proxy  
- Use Gunicorn for Flask (production)  
- Deploy on AWS / Render  

---

Author

Ritik Batho  
https://github.com/ritikbatho16  

---

