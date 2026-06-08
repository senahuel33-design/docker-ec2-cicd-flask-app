# Dockerized Flask App on AWS EC2 with CI/CD

This project demonstrates how to deploy a Dockerized Python Flask application to AWS EC2 and automate deployments using GitHub Actions.

The application is containerised with Docker, hosted on an EC2 instance, and automatically redeployed whenever code is pushed to GitHub.

The project includes:
- Docker containerization
- Automated CI/CD with GitHub Actions
- AWS EC2 deployment
- Infrastructure automation (Terraform - in progress)
- Secure deployment workflow

  
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
![Flask Code](<Screenshots/Flask app/Flask Application Code.PNG>)

## Flask Application Running
![Flask Running](<Screenshots/Flask app/Flask Application Running.PNG>)

## Browser Test
![Browser Test](<Screenshots/Flask app/Flask app running in terminal.PNG>)

---

# Step 2 – Dockerize the Flask Application

The Flask application was containerized using Docker to ensure consistent deployment across environments.

## Dockerfile
![Dockerfile](<Screenshots/Docker/Dockerfile.PNG>)

## Docker Build Success
![Docker Build](<Screenshots/Docker/Docker build success.PNG>)

## Running Docker Container
![Docker Container](<Screenshots/Docker/Running Docker Container.PNG>)

## Docker Process Audit (Container List)
![Docker PS](<Screenshots/Docker/Docker ps.PNG>)

## Browser Test via Localhost Loopback
![Docker Browser Test](<Screenshots/Docker/Browser test.PNG>)

---

# Step 3 – Deploy Docker Container to AWS EC2

Launched an EC2 instance and deployed the Dockerized Flask application to the cloud.

## EC2 Instance Created
![EC2 Instance](<Screenshots/Deploy Docker Container to AWS EC2/ec2-instance-active.png>)

## SSH Connection to EC2
![SSH Connection](<Screenshots/Deploy Docker Container to AWS EC2/ec2-ssh-connection.png>)

## EC2 Security Group Configuration
![Security Group](<Screenshots/Deploy Docker Container to AWS EC2/security-group-config.png>)

## Docker Installed on EC2
![Docker EC2](<Screenshots/CICD/docker-installed.png>)

## Running Docker Container on EC2
![Docker EC2 Running](<Screenshots/CICD/docker-installed.png>)

## Public EC2 Deployment
![EC2 Deployment](<Screenshots/CICD/deployment-verification.png>)

---

# Step 4 – Configure GitHub Actions CI/CD

Configured GitHub Actions to automatically deploy the application to the EC2 instance after every push to the repository.

## GitHub Actions Workflow
![GitHub Actions](<Screenshots/Configure GitHub Actions CI/github-actions-workflow.png>)

## Successful CI/CD Deployment
![CI/CD Success](<Screenshots/Configure GitHub Actions CI/successful-cicd-deployment.png>)
URL : http://3.255.113.69:5000
---

# Step 5 – Terraform Infrastructure Automation

Terraform was used to automate AWS infrastructure provisioning.

## Terraform Resources
- EC2 Instance
- Security Groups
- Amazon ECR Repository

## Terraform Initialization
![Terraform Init](<Screenshots/Terraform/terraform-init.png>)

## Terraform Apply
![Terraform Apply](<Screenshots/Terraform/terraform-apply.png>)

## EC2 Created with Terraform
![Terraform EC2](<Screenshots/Terraform/terraform-ec2.png>)
