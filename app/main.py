from fastapi import FastAPI
from models.business import BusinessIdea

app = FastAPI(
    title="Guidara AI",
    description="AI-powered business idea validation platform",
    version="1.0.0"
)

business_ideas = []

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

@app.post("/business-ideas")
def create_business_idea(idea: BusinessIdea):
    business_ideas.append(idea)
    return {
        "message": "Business idea created successfully",
        "data": idea
    }

@app.get("/business-ideas")
def get_business_ideas():
    return {
        "count": len(business_ideas),
        "data": business_ideas
    }