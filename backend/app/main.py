from fastapi import FastAPI
from app.services.farming_advice import get_farming_advice

app = FastAPI(
    title="KhetPulse AI",
    description="AI-powered multilingual farming assistant for Indian farmers",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "KhetPulse AI",
        "message": "Welcome to KhetPulse AI!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "KhetPulse AI"
    }
@app.get("/farming-advice")
def farming_advice(crop: str):
    return get_farming_advice(crop)
