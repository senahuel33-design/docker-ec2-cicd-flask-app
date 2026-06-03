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

# Step 1 – Create Flask Application

Created a simple Flask web application running locally.

## Flask Application Code
![Flask Code](<screenshots/local/flask-code.png>)

## Flask Application Running
![Flask Running](<screenshots/local/flask-terminal-running.png>)

## Browser Test
![Browser Test](<screenshots/local/flask-browser-test.png>)

---

# Step 2 – Dockerize the Flask Application

The Flask application was containerized using Docker to ensure consistent deployment across environments.

## Dockerfile
![Dockerfile](<screenshots/docker/dockerfile.png>)

## Docker Build Success
![Docker Build](<screenshots/docker/docker-build-success.png>)

## Running Docker Container
![Docker Container](<screenshots/docker/docker-container-running.png>)

## Docker Process Audit (Container List)
![Docker PS](<screenshots/docker/docker-ps.png>)

## Browser Test via Localhost Loopback
![Docker Browser Test](<screenshots/docker/docker-browser-test.png>)

---

# Step 3 – Deploy Docker Container to AWS EC2

Launched an EC2 instance and deployed the Dockerized Flask application to the cloud.

## EC2 Instance Created
![EC2 Instance](<screenshots/ec2/ec2-instance-created.png>)

## SSH Connection to EC2
![SSH Connection](<screenshots/ec2/ssh-connection.png>)

## EC2 Security Group Configuration
![Security Group](<screenshots/ec2/security-group.png>)

## Docker Installed on EC2
![Docker EC2](<screenshots/ec2/docker-installed-ec2.png>)

## Running Docker Container on EC2
![Docker EC2 Running](<screenshots/ec2/docker-ec2-running.png>)

## Public EC2 Deployment
![EC2 Deployment](<screenshots/ec2/ec2-public-access.png>)

---

# Step 4 – Configure GitHub Actions CI/CD

Configured GitHub Actions to automatically deploy the application to the EC2 instance after every push to the repository.

## GitHub Actions Workflow
![GitHub Actions](<screenshots/cicd/github-actions-workflow.png>)

## Successful CI/CD Deployment
![CI/CD Success](<screenshots/cicd/github-actions-success.png>)

---

# Step 5 – Future Improvements

Planned improvements for future versions of the project:

- Add Nginx reverse proxy
- Add HTTPS support
- Add custom domain
- Add monitoring and logging
- Automate infrastructure with Terraform
