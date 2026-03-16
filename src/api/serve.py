from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(title="Enterprise Predictive API", version="1.0.0")

class SensorData(BaseModel):
    sensor_1: float
    sensor_2: float
    sensor_3: float
    sensor_4: float
    sensor_5: float

try:
    # Attempt to load model if it exists
    model = joblib.load("model_artifact.pkl")
except:
    model = None

@app.post("/api/v1/predict")
async def predict_failure(data: SensorData):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not initialized. Run train.py first.")
    
    features = np.array([[data.sensor_1, data.sensor_2, data.sensor_3, data.sensor_4, data.sensor_5]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "status": "success",
        "failure_prediction": bool(prediction),
        "confidence_score": float(probability),
        "recommendation": "Initiate maintenance" if prediction else "Continue normal operation"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}
