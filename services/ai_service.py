import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def analyze_business_idea(idea):
    if client is None:
        return {
            "business_name": idea.business_name,
            "market_analysis": "AI service is not configured in this environment.",
            "risk_score": 0,
            "success_probability": 0,
            "competition_level": "Unknown",
            "swot_analysis": {
                "strengths": [],
                "weaknesses": [],
                "opportunities": [],
                "threats": []
            },
            "recommendations": [],
            "financial_advice": "No API key configured.",
            "marketing_strategy": "No API key configured.",
            "final_recommendation": "Configure OPENAI_API_KEY to enable AI analysis."
        }

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