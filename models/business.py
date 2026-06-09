from pydantic import BaseModel

class BusinessIdea(BaseModel):
    business_name: str
    industry: str
    budget: float
    location: str
    target_audience: str
    description: str