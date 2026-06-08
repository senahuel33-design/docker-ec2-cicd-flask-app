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

This stage represented the most challenging phase of the project, as resolving configuration discrepancies from earlier setup steps required meticulous, iterative troubleshooting. The primary engineering bottleneck involved configuring the precise IAM policies and Security Group rules necessary to establish secure, seamless interconnection between the AWS services, ultimately enabling the application to run smoothly.

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

## Issues 

1. GitHub Actions OIDC Handshake Authentication Failure.
   
Error Message: Could not assume role with OIDC: Not authorized to perform sts:AssumeRoleWithWebIdentity

Context: Occurred during the initial authentication step (Configure AWS Credentials) inside the GitHub Actions runner.
![Handshake Authentication Failure](<Screenshots/Mistakes/OpenID Connect (OIDC) handshake error.png>

Resolution: * Updated the Trust Relationship JSON Document inside the deployment IAM role.

Verified that the condition block explicitly allowed sts:AssumeRoleWithWebIdentity from the official GitHub Identity Provider (token.actions.githubusercontent.com).

Scoped the audience condition (aud) to sts.amazonaws.com and strictly bound the resource claim to the correct repository path (repo:senahuel33-design/docker-ec2-cicd-flask-app:*).
![Updated the Trust Relationship JSON Document](<Screenshots/Mistakes/OpenID Connect (OIDC) handshake error.png>)

2. AWS Systems Manager (SSM) Target Node State Error

Error Message: Error: aws: [ERROR]: An error occurred (InvalidInstanceId) when calling the SendCommand operation: Instances not in a valid state for account

Context: Occurred during the remote execution step (Deploy to EC2 via AWS Systems Manager (SSM)).
![(SSM) Target Node State Error](<Screenshots/Mistakes/Instances not in a valid state for account.png>)
Root Cause: This error occurs under two conditions: either the deployment script is targeting a hardcoded or incorrect Instance ID that does not exist in the region, or the target EC2 server hasn't been picked up by the Systems Manager inventory. Without the AmazonSSMManagedInstanceCore policy attached to the server's IAM instance profile, the SSM agent daemon running inside Ubuntu cannot check in with the AWS backend control plane, rendering it "invisible" to automated terminal commands.

Resolution:

Attached the AmazonSSMManagedInstanceCore AWS managed policy directly to the instance profile role bound to the EC2 host.

Audited the live compute dashboard to retrieve the precise operational Instance ID.

Corrected the target configuration payload inside the workflow block (--targets "Key=instanceids,Values=i-0eafb72d55f61da97") to map execution requests directly to the active node.

## Lessons Learned

- Managing Docker containers in cloud environments
- Configuring GitHub Actions secrets securely
- Troubleshooting EC2 networking and security groups
- Understanding CI/CD automation workflows
