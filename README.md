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

The project is built using modern DevOps and Cloud-Native principles and demonstrates:

- Asynchronous microservice communication  
- Cloud service simulation (AWS SQS via LocalStack)  
- Containerization & orchestration with Kubernetes  
- Full CI/CD automation pipeline  
- Observability with real-time metrics  

---

## 🏗️ Architecture & Tech Stack (What & Why)

Each technology is carefully selected to reflect real-world enterprise scenarios.

### 1️⃣ Microservices & Asynchronous Communication  
**(Python Flask & LocalStack SQS)**  

- **Order API**: RESTful API handling incoming user requests  
- **Why LocalStack SQS?**  
  - Simulates AWS services locally without cost  
  - Enables asynchronous communication between microservices  
  - Eliminates dependency on real cloud accounts  

---

### 2️⃣ Containerization & Orchestration  
**(Docker & Kubernetes / Minikube)**  

- All services are containerized using Docker  
- Kubernetes provides:
  - High Availability  
  - Self-Healing  
  - Scalability  

- Managed via:
  - Deployments  
  - Services  
  - ReplicaSets  

---

### 3️⃣ Observability & Monitoring  
**(Prometheus & Grafana)**  

- Prometheus metrics are integrated into API endpoints  
- Real-time monitoring of system performance  

**Why ServiceMonitor?**
- Enables automatic service discovery in Kubernetes  
- Uses Prometheus Operator & CRDs (Custom Resource Definitions)  

---

### 4️⃣ CI/CD Automation  
**(GitHub Actions & Self-Hosted ARM64 Runner)**  

- Fully automated CI/CD pipeline triggered on every push  

**Architecture Challenge Solved:**
- Project developed on **Apple Silicon (M3 Pro ARM64)**  
- Default cloud runners (x64) caused compatibility issues  

✅ Solution:
- Integrated MacBook M3 Pro as a **Self-Hosted Runner**  
- Native builds with full performance  
- Eliminated Docker socket & architecture conflicts  

---

## 📸 Project Showcase

### 🟢 1. GitHub Actions — End-to-End CI/CD

- Pipeline automatically triggered on push  
- Build executed on Self-Hosted Runner  
- Docker image built & deployed to Minikube  
- Total pipeline time: **~1 min 17 sec**
<img width="1512" height="860" alt="Ekran Resmi 2026-03-20 21 29 17" src="https://github.com/user-attachments/assets/9708e7c0-cc5f-4957-94af-c87abdbca5a1" />
<img width="1512" height="949" alt="Ekran Resmi 2026-03-20 21 56 34" src="https://github.com/user-attachments/assets/de9a6677-5a3b-46a0-8f53-c0770f6d7434" />

---

### ☁️ 2. AWS Cloud Simulation — LocalStack SQS  

- Fully local AWS simulation without cost  
- `order-events` queue successfully created and listed  
<img width="1512" height="949" alt="Ekran Resmi 2026-03-20 21 36 11" src="https://github.com/user-attachments/assets/8b593142-a961-46ad-bb01-816b96ee3ed9" />

---

### ☸️ 3. Kubernetes Orchestration  

- `kubectl get all` output confirms:
  - Pods running  
  - Services active  
  - ReplicaSets healthy  
<img width="1512" height="949" alt="Ekran Resmi 2026-03-20 21 29 47" src="https://github.com/user-attachments/assets/0d71355d-7731-4b99-b8d8-ed80a523ec49" />

---

### 📈 4. Observability — Prometheus Targets  

- `order-api-monitor` ServiceMonitor successfully detected  
- Metrics endpoint:
  ```
  10.244.0.36:5001/metrics
  ```
- Status: **UP** ✅  
<img width="1512" height="860" alt="Ekran Resmi 2026-03-20 21 31 59" src="https://github.com/user-attachments/assets/7d3ec893-fc90-44c4-b70e-b9f9ca334d3b" />

---

### 🐳 5. Docker Ecosystem  

- LocalStack  
- Minikube  
- Custom Order API container  

All running seamlessly in Docker environment  
<img width="1512" height="949" alt="Ekran Resmi 2026-03-20 21 39 08" src="https://github.com/user-attachments/assets/a325d1c0-a8f3-4cb1-89fa-7f515a012368" />
<img width="1512" height="949" alt="Ekran Resmi 2026-03-20 21 38 40" src="https://github.com/user-attachments/assets/01da6758-a165-414f-a795-c1e60967fbea" />

---

# 🚀 Setup & Installation Guide  

Follow these steps to run the project locally.

---

## ⚙️ Prerequisites  

- Docker & Docker Desktop  
- Minikube & kubectl  
- Python 3.9+  
- AWS CLI (`aws` & `awslocal`)  

---

## 1️⃣ Clone the Repository  

```
git clone https://github.com/YOUR_USERNAME/omni-ops.git
cd omni-ops
```

---

## 2️⃣ (Optional) Fork via CLI  

```
gh repo fork YOUR_USERNAME/omni-ops --clone=true
```

---

## 3️⃣ Start LocalStack (AWS Simulation)  

```
docker-compose up -d localstack
```

### Create SQS Queue  

```
aws --endpoint-url=http://localhost:4566 sqs create-queue \
--queue-name order-events \
--region us-east-1
```

---

## 4️⃣ Start Kubernetes Cluster  

```
minikube start --driver=docker
```

### Deploy Order API  

```
kubectl apply -f k8s/apps/order-api/deployment.yaml
kubectl apply -f k8s/apps/order-api/service.yaml
```

---

## 5️⃣ Setup Monitoring (Prometheus)  

```
kubectl apply -f k8s/apps/order-api/servicemonitor.yaml
```

### Verify Pods  

```
kubectl get pods
```

---

## 6️⃣ Trigger CI/CD Pipeline (Optional)  

```
git add .
git commit -m "feat: add new feature"
git push origin main
```

If Self-Hosted Runner is active → pipeline runs automatically 🚀  

---

## 🧠 Key Capabilities  

- Full SDLC simulation  
- Asynchronous microservices  
- Cloud-native architecture  
- Kubernetes orchestration  
- Real-time observability  
- Production-like CI/CD pipeline  

---

## 👨‍💻 Developer  

**Ali Gaffar Toksoy**  
Computer Engineering Student | Zonguldak Bülent Ecevit University  

Passionate about:  
- DevOps  
- Cloud Computing  
- Microservices Architecture  

> "Don't just write code — design how it will run, scale, and survive."  

---
