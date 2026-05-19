# Dockerized Flask App on AWS EC2 with CI/CD

This project demonstrates how to deploy a Dockerized Python Flask application to AWS EC2 and automate deployments using GitHub Actions.

The application is containerised with Docker, hosted on an EC2 instance, and automatically redeployed whenever code is pushed to GitHub.

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
