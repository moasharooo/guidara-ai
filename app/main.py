from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import engine, SessionLocal
from models.business import Base, BusinessIdeaDB, BusinessIdeaCreate
from services.ai_service import analyze_business_idea
from app.dashboard import dashboard_page
import json

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Guidara AI",
    description="AI-powered business idea validation platform",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
def create_business_idea(idea: BusinessIdeaCreate, db: Session = Depends(get_db)):
    new_idea = BusinessIdeaDB(
        business_name=idea.business_name,
        industry=idea.industry,
        budget=idea.budget,
        location=idea.location,
        target_audience=idea.target_audience,
        description=idea.description
    )

    db.add(new_idea)
    db.commit()
    db.refresh(new_idea)

    return {
        "message": "Business idea created successfully",
        "data": {
            "id": new_idea.id,
            "business_name": new_idea.business_name,
            "industry": new_idea.industry,
            "budget": new_idea.budget,
            "location": new_idea.location,
            "target_audience": new_idea.target_audience,
            "description": new_idea.description
        }
    }

@app.get("/business-ideas")
def get_business_ideas(db: Session = Depends(get_db)):
    ideas = db.query(BusinessIdeaDB).all()

    return {
        "count": len(ideas),
        "data": ideas
    }

@app.post("/analyze/{idea_id}")
def analyze_idea(idea_id: int, db: Session = Depends(get_db)):
    idea = db.query(BusinessIdeaDB).filter(BusinessIdeaDB.id == idea_id).first()

    if idea is None:
        return {
            "error": "Business idea not found"
        }

    analysis = analyze_business_idea(idea)

    idea.analysis = json.dumps(analysis)
    db.commit()
    db.refresh(idea)

    return {
        "message": "Business idea analyzed and saved successfully",
        "analysis": analysis
    }

@app.get("/business-ideas/{idea_id}")
def get_business_idea(idea_id: int, db: Session = Depends(get_db)):
    idea = db.query(BusinessIdeaDB).filter(BusinessIdeaDB.id == idea_id).first()

    if idea is None:
        return {
            "error": "Business idea not found"
        }

    return {
        "id": idea.id,
        "business_name": idea.business_name,
        "industry": idea.industry,
        "budget": idea.budget,
        "location": idea.location,
        "target_audience": idea.target_audience,
        "description": idea.description,
        "analysis": json.loads(idea.analysis) if idea.analysis else None
    }

@app.delete("/business-ideas/{idea_id}")
def delete_business_idea(idea_id: int, db: Session = Depends(get_db)):
    idea = db.query(BusinessIdeaDB).filter(BusinessIdeaDB.id == idea_id).first()

    if idea is None:
        return {"error": "Business idea not found"}

    db.delete(idea)
    db.commit()

    return {"message": "Business idea deleted successfully"}


@app.get("/dashboard")
def dashboard():
    return dashboard_page()