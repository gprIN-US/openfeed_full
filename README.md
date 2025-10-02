# OpenFeed – Full Bundle (All Milestones)

This bundle gives you a **working end-to-end skeleton** with unique ports so it won’t clash with other projects.

## Ports (non-standard to avoid conflicts)
- FastAPI ranker: **8091** (Docker) or **8092** (local `serve-local`)
- Kafka (host): **29093**
- Zookeeper: **22181**
- Redis: **6380**
- MinIO: **9002** (API), **9003** (Console)
- MLflow: **5001**
- Prometheus: **9097**
- Grafana: **3001**

## Quickstart

1) Start Docker stack
```bash
make up
```

2) Create Kafka topic
```bash
make topics
```

3) Generate live events
```bash
make gen
```

4) (Optional) Consume to verify
```bash
make consume
```

5) Train a baseline model and export to `serving/api/model.pkl` (also logs to MLflow)
```bash
make train
```

6) Rank API
- Docker service: http://localhost:8091/healthz
- Local dev (no Docker): `make serve-local` → http://localhost:8092/healthz

### Example rank request
```bash
curl -X POST http://localhost:8091/rank -H "Content-Type: application/json" -d '{
  "user_id": "user_1",
  "candidate_ids": ["i1","i2","i3"],
  "features": [[0.1,0.2,0.3,0.4,0.5],[0.5,0.4,0.3,0.2,0.1],[0.9,0.1,0.2,0.1,0.0]]
}'
```

## Notes
- This bundle focuses on **working components** (ingestion, simple training, serving, metrics). Spark/Feast are intentionally omitted to keep setup light and reliable on a laptop. We can add them later.
- Prometheus scrapes FastAPI metrics at `http://localhost:8091/metrics`. Grafana listens on `http://localhost:3001` (login: admin/admin).

Enjoy 🚀
