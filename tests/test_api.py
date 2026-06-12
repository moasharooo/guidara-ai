from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath("."))

from app.main import app
client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Guidara AI"

def test_create_business_idea():
    payload = {
        "business_name": "Test Coffee",
        "industry": "Food & Beverage",
        "budget": 10000,
        "location": "Irbid",
        "target_audience": "Students",
        "description": "A test business idea"
    }

    response = client.post("/business-ideas", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Business idea created successfully"
    assert response.json()["data"]["business_name"] == "Test Coffee"