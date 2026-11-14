from fastapi import FastAPI

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
