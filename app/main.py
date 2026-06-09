from fastapi import FastAPI

app = FastAPI(
    title="Guidara AI",
    description="AI-powered business idea validation platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Guidara AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }