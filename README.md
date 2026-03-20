# 🚀 Omni-Ops: Enterprise Cloud-Native DevOps Ecosystem

<div align="center">
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" />
<img src="https://img.shields.io/badge/LocalStack-FFFFFF?style=for-the-badge&logo=localstack&logoColor=black" />
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
<img src="https://img.shields.io/badge/Python_Flask-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</div>

---

## 🌍 Overview

Omni-Ops is an **enterprise-grade cloud-native DevOps ecosystem** that simulates the full Software Development Life Cycle (SDLC) — from code creation to deployment, orchestration, and real-time monitoring.

The project demonstrates:

- Asynchronous microservice communication  
- Cloud service simulation (AWS SQS via LocalStack)  
- Containerization & orchestration with Kubernetes  
- Fully automated CI/CD pipelines  
- Observability with real-time metrics  

---

## 📂 Project Structure  

```
omni-ops/
├── Makefile                     # Automation commands (e.g., make deploy)
├── docker-compose.yml           # LocalStack (AWS simulation) & local environment
├── requirements.txt             # Global Python dependencies
│
├── infrastructure/              # 🏗️ Infrastructure as Code
│   └── terraform/
│       ├── main.tf              # Core infrastructure resources
│       ├── provider.tf          # AWS / LocalStack provider configuration
│       └── variables.tf         # Terraform variables
│
├── k8s/                         # ☸️ Kubernetes manifests
│   ├── apps/
│   │   ├── invoice-worker/      # Worker service K8s configs
│   │   │   └── deployment.yaml
│   │   └── order-api/           # API service K8s configs
│   │       ├── deployment.yaml
│   │       ├── localstack-bridge.yaml
│   │       ├── service.yaml
│   │       └── servicemonitor.yaml  # Prometheus monitoring config
│   └── argocd/                  # (Optional) GitOps continuous delivery configs
│
├── monitoring/                  # 📈 Observability layer
│   ├── grafana/                 # Dashboard configurations
│   └── prometheus/              # Metrics collection rules
│
├── services/                    # 💻 Microservices source code
│   ├── invoice-worker/          # Async worker consuming SQS messages
│   │   ├── Dockerfile
│   │   └── worker.py
│   └── order-api/               # Flask API handling user requests
│       ├── Dockerfile
│       ├── app.py
│       └── requirements.txt
│
├── venv/                        # 📦 Python environment (ignored)
└── volume/                      # 💾 LocalStack persistent data & logs (ignored)
```

---

## 🏗️ Architecture & Tech Stack (What & Why)

Each technology is carefully selected to reflect real-world enterprise scenarios.

### 1️⃣ Microservices & Asynchronous Communication  
**(Python Flask & LocalStack SQS)**  

- **Order API**: RESTful API handling incoming requests  
- **Invoice Worker**: Background service consuming queue messages  

**Why LocalStack SQS?**
- Simulates AWS services locally without cost  
- Enables asynchronous communication  
- Removes dependency on real cloud accounts  

---

### 2️⃣ Containerization & Orchestration  
**(Docker & Kubernetes / Minikube)**  

- All services are containerized using Docker  
- Kubernetes provides:
  - High Availability  
  - Self-Healing  
  - Scalability  

Managed via:
- Deployments  
- Services  
- ReplicaSets  

---

### 3️⃣ Observability & Monitoring  
**(Prometheus & Grafana)**  

- Prometheus metrics exposed via API endpoints  
- Real-time monitoring of system performance  

**Why ServiceMonitor?**
- Enables automatic service discovery  
- Uses Prometheus Operator & CRDs  

---

### 4️⃣ CI/CD Automation  
**(GitHub Actions & Self-Hosted ARM64 Runner)**  

- Pipeline runs automatically on every push  

**Architecture Challenge Solved:**
- Apple Silicon (M3 Pro ARM64) vs x64 runner mismatch  

✅ Solution:
- Self-hosted runner on MacBook M3 Pro  
- Native builds  
- Eliminated Docker/socket issues  

---

## 📸 Project Showcase

### 🟢 GitHub Actions — CI/CD Pipeline  

<img src="https://github.com/user-attachments/assets/9708e7c0-cc5f-4957-94af-c87abdbca5a1" />
<img src="https://github.com/user-attachments/assets/de9a6677-5a3b-46a0-8f53-c0770f6d7434" />

---

### ☁️ LocalStack SQS  

<img src="https://github.com/user-attachments/assets/8b593142-a961-46ad-bb01-816b96ee3ed9" />

---

### ☸️ Kubernetes  

<img src="https://github.com/user-attachments/assets/0d71355d-7731-4b99-b8d8-ed80a523ec49" />

---

### 📈 Prometheus  

<img src="https://github.com/user-attachments/assets/7d3ec893-fc90-44c4-b70e-b9f9ca334d3b" />

---

### 🐳 Docker  

<img src="https://github.com/user-attachments/assets/a325d1c0-a8f3-4cb1-89fa-7f515a012368" />
<img src="https://github.com/user-attachments/assets/01da6758-a165-414f-a795-c1e60967fbea" />

---

# 🚀 Setup & Installation Guide  

## ⚙️ Prerequisites  

- Docker & Docker Desktop  
- Minikube & kubectl  
- Python 3.9+  
- AWS CLI (`aws` & `awslocal`)  

---

## 1️⃣ Clone Repository  

```
git clone https://github.com/YOUR_USERNAME/omni-ops.git
cd omni-ops
```

---

## 2️⃣ (Optional) Fork  

```
gh repo fork YOUR_USERNAME/omni-ops --clone=true
```

---

## 3️⃣ Start LocalStack  

```
docker-compose up -d localstack
```

### Create Queue  

```
aws --endpoint-url=http://localhost:4566 sqs create-queue \
--queue-name order-events \
--region us-east-1
```

---

## 4️⃣ Start Kubernetes  

```
minikube start --driver=docker
```

```
kubectl apply -f k8s/apps/order-api/deployment.yaml
kubectl apply -f k8s/apps/order-api/service.yaml
```

---

## 5️⃣ Setup Monitoring  

```
kubectl apply -f k8s/apps/order-api/servicemonitor.yaml
kubectl get pods
```

---

## 6️⃣ Trigger CI/CD  

```
git add .
git commit -m "feat: update"
git push origin main
```

---

## 🧠 Key Capabilities  

- End-to-end SDLC simulation  
- Async microservices architecture  
- Kubernetes-native deployment  
- Real-time observability  
- Production-grade CI/CD  

---

## 👨‍💻 Developer  

**Ali Gaffar Toksoy**  
Computer Engineering Student | Zonguldak Bülent Ecevit University  

Passionate about:
- DevOps  
- Cloud Computing  
- Microservices  

> "Don't just write code — design how it runs, scales, and survives."  

---
