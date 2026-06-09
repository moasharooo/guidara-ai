from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class BusinessIdeaDB(Base):
    __tablename__ = "business_ideas"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, index=True)
    industry = Column(String)
    budget = Column(Float)
    location = Column(String)
    target_audience = Column(String)
    description = Column(String)

class BusinessIdeaCreate(BaseModel):
    business_name: str
    industry: str
    budget: float
    location: str
    target_audience: str
    description: str