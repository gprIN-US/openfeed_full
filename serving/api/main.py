from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import os
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time
import random
import joblib

app = FastAPI(title="OpenFeed Ranker")

# Prometheus metrics
req_counter = Counter("requests_total", "Total requests", ["endpoint"])
latency_hist = Histogram("request_latency_ms", "Latency in ms", ["endpoint"])

# Optional sklearn model
MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")
_model = None
if os.path.exists(MODEL_PATH):
    try:
        _model = joblib.load(MODEL_PATH)
        print("Loaded model:", MODEL_PATH)
    except Exception as e:
        print("Could not load model:", e)

class RankRequest(BaseModel):
    user_id: str
    candidate_ids: List[str]
    features: Optional[List[List[float]]] = None  # optional per-candidate features

class RankResponse(BaseModel):
    ids: List[str]
    scores: List[float]

@app.get("/healthz")
def healthz():
    req_counter.labels("/healthz").inc()
    return {"status": "ok", "message": "FastAPI is running"}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

@app.post("/rank", response_model=RankResponse)
def rank(req: RankRequest):
    t0 = time.time()
    req_counter.labels("/rank").inc()

    # If a model exists and features provided, score with model (expects 2D list)
    scores = []
    if _model and req.features:
        try:
            scores = [float(s) for s in _model.predict_proba(req.features)[:,1]]
        except Exception as e:
            # fallback
            scores = [random.random() for _ in req.candidate_ids]
    else:
        scores = [random.random() for _ in req.candidate_ids]

    # sort by score desc
    pairs = sorted(zip(req.candidate_ids, scores), key=lambda x: x[1], reverse=True)
    out_ids = [p[0] for p in pairs]
    out_scores = [p[1] for p in pairs]

    latency_hist.labels("/rank").observe((time.time()-t0)*1000.0)
    return RankResponse(ids=out_ids, scores=out_scores)
