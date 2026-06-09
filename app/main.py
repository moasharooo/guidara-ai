from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import engine, SessionLocal
from models.business import Base, BusinessIdeaDB, BusinessIdeaCreate

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