import os, random
import numpy as np
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib

# synthesize small dataset
random.seed(0)
np.random.seed(0)
X = np.random.randn(1000, 5)
y = (X[:,0]*0.8 + X[:,1]*0.4 + np.random.randn(1000)*0.5 > 0).astype(int)

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5001"))
mlflow.set_experiment("openfeed_baseline")

with mlflow.start_run():
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    proba = model.predict_proba(X)[:,1]
    auc = roc_auc_score(y, proba)
    mlflow.log_metric("auc", float(auc))
    os.makedirs("serving/api", exist_ok=True)
    joblib.dump(model, "serving/api/model.pkl")
    mlflow.log_artifact("serving/api/model.pkl")
    print("Trained model saved to serving/api/model.pkl with AUC:", auc)
