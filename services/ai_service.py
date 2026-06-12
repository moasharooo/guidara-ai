import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_business_idea(idea):
    prompt = f"""
You are Guidara AI, an expert business validation advisor.

Analyze this business idea and return ONLY valid JSON.

Business Name: {idea.business_name}
Industry: {idea.industry}
Budget: {idea.budget}
Location: {idea.location}
Target Audience: {idea.target_audience}
Description: {idea.description}

Return this exact JSON structure:
{{
  "business_name": "...",
  "market_analysis": "...",
  "risk_score": 0,
  "success_probability": 0,
  "competition_level": "...",
  "swot_analysis": {{
    "strengths": [],
    "weaknesses": [],
    "opportunities": [],
    "threats": []
  }},
  "recommendations": [],
  "financial_advice": "...",
  "marketing_strategy": "...",
  "final_recommendation": "..."
}}
"""

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    try:
        text = response.output_text.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception:
        return {
            "error": "Failed to parse OpenAI response",
            "raw_response": response.output_text
        }