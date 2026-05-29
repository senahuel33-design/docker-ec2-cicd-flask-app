# Dockerized Flask App on AWS EC2 with CI/CD

This project demonstrates how to deploy a Dockerized Python Flask application to AWS EC2 and automate deployments using GitHub Actions.

The application is containerised with Docker, hosted on an EC2 instance, and automatically redeployed whenever code is pushed to GitHub.

## Architecture
Developer → GitHub → GitHub Actions → AWS EC2 → Users
![Architecture](<Architecture/Architecture.png>)

docker-ec2-cicd-flask-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│
├── .github/
│   └── workflows/
│
├── screenshots/
│   ├── ec2/
│   ├── docker/
│   ├── cicd/
│   └── solutions/
│
├── architecture/
│
├── Dockerfile
│
└── README.md

## Step 1 – Create Flask Application

Created a simple Flask web application running locally.

### Flask Application Code
![Flask Code](<Screenshots/Flask app/Flask Application Code.PNG>)

### Flask Application Running
![Flask Running](<Screenshots/Flask app/Flask Application Running.PNG>)

### Browser Test
![Browser Test](<Screenshots/Flask app/Flask app running in terminal.PNG>)

---

## Step 2 – Dockerize the Flask Application

The Flask application was containerized using Docker to ensure consistent deployment across environments.

### Dockerfile

![Dockerfile](<Screenshots/Docker/Dockerfile.PNG>)

### Docker Build Success

![Docker Build](<Screenshots/Docker/Docker build success.PNG>)

![Docker Build](<Screenshots/Docker/Docker build success 1.PNG>)

### Running Docker Container

![Docker Container](<Screenshots/Docker/Running Docker Container.PNG>)

### Docker Container List

![Docker PS](<Screenshots/Docker/Docker ps.PNG>)

### Browser Test via Docker

![Docker Browser Test](<Screenshots/Docker/Browser test.PNG>)

---

## Step 3 – Local Containerization & Verification

The Flask application environment was systematically validated and executed locally using Docker Desktop integrated with a WSL2 (Ubuntu) backend.

### Docker Build Success
The multi-layer image compilation completed successfully, resolving all background dependencies and verifying structural build definitions.

![Docker Build](<Docker/docker-build-success.png>)

### Running Docker Container
The compiled image was instantiated into an active local runtime session, initializing the internal WSGI micro-framework server.

![Docker Container](<Docker/docker-container-running.png>)

### Browser Test via Localhost Loopback
Network routing protocols were audited across the WSL2 bridge by verifying the active user interface via a host browser loopback session at port `5000`.

![Docker Browser Test](<Docker/app-live.png>)

### Docker Process Audit (Container List)
An explicit container engine inspection was executed to validate continuous runtime stability, uptime metrics, and absolute port binding parity.

![Docker PS](<Docker/docker-ps.png>)

---
