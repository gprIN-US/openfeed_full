#  OpenFeed  End-to-End Recommendation & Evaluation System

An **end-to-end ML + Data Engineering pipeline** with:
- ✅ Synthetic data generation & Kafka streaming  
- ✅ Model training & tracking with MLflow  
- ✅ FastAPI microservice for online serving  
- ✅ Monitoring with Prometheus + Grafana  
- ✅ Counterfactual evaluation (IPS, SNIPS, DR)

This project showcases **real-world Data Science + Data Engineering + MLOps** skills.

---

##  Features
- **Data Ingestion** → Generate synthetic user-item events with Kafka  
- **Stream Processing** → Kafka + Redis + MinIO backbone  
- **Model Training** → Scikit-learn model logged to MLflow  
- **Serving** → FastAPI microservice (`/rank`, `/healthz`, `/metrics`)  
- **Monitoring** → Prometheus & Grafana dashboards  
- **Evaluation** → IPS, SNIPS, DR estimators for counterfactual learning  

---

##  Architecture

Data Generator → Kafka → ML Training (MLflow) → Model (FastAPI)
↓
Prometheus / Grafana (Monitoring)
↓
Evaluation Scripts


---

##  Tech Stack
- **Infrastructure** → Docker, Docker Compose  
- **Streaming** → Kafka + Zookeeper  
- **Storage** → Redis + MinIO  
- **MLOps** → MLflow (tracking), FastAPI (serving)  
- **Monitoring** → Prometheus + Grafana  
- **ML** → Scikit-learn, Python  

---

##  Getting Startedd

### 1️⃣ Clone repo
```bash
git clone https://github.com/gprIN-US/openfeed_full.git
cd openfeed_full
2️⃣ Start stack
make up
3️⃣ Create Kafka topic
make topics
4️⃣ Generate events
make gen
5️⃣ Consume events
make consume
6️⃣ Train model & log to MLflow
make train
7️⃣ Serve API locally
make serve-local
Visit: http://localhost:8092/healthz
Example API Call
curl -X POST http://localhost:8091/rank -H "Content-Type: application/json" -d '{
  "user_id": "user_1",
  "candidate_ids": ["i1","i2","i3"],
  "features": [[0.1,0.2,0.3,0.4,0.5],[0.5,0.4,0.3,0.2,0.1],[0.9,0.1,0.2,0.1,0.0]]
}'
Monitoring & Dashboards
MLflow → http://localhost:5001
Grafana → http://localhost:3001 (login: admin/admin)
Prometheus → http://localhost:9097
 Why this project matters
This project demonstrates end-to-end ownership of a modern ML system:
Data Pipelines → Kafka, Redis, MinIO
MLOps → MLflow, FastAPI serving
Monitoring → Prometheus, Grafana
Evaluation → IPS, SNIPS, DR for bandit feedback
this guys, should/will be a complete system: ingestion → training → serving → monitoring.
👤 Author
Built with ❤️ by Prerna Reddy G


