def analyze_business_idea(idea):
    risk_score = 50

    if idea.budget < 10000:
        risk_score += 20
    elif idea.budget > 30000:
        risk_score -= 10

    if "coffee" in idea.business_name.lower() or "food" in idea.industry.lower():
        competition_level = "High"
        risk_score += 10
    else:
        competition_level = "Medium"

    if risk_score > 100:
        risk_score = 100
    if risk_score < 0:
        risk_score = 0

    success_probability = 100 - risk_score

    return {
        "business_name": idea.business_name,
        "market_opportunity": "Medium-High",
        "competition_level": competition_level,
        "risk_score": risk_score,
        "success_probability": success_probability,
        "swot_analysis": {
            "strengths": [
                "Clear target audience",
                "Defined business location",
                "Initial budget available"
            ],
            "weaknesses": [
                "Limited real market data in MVP version",
                "Competition requires strong differentiation"
            ],
            "opportunities": [
                "Potential to attract niche customers",
                "Can improve pricing and marketing strategy"
            ],
            "threats": [
                "High competition",
                "Changing customer behavior",
                "Unexpected operational costs"
            ]
        },
        "recommendations": [
            "Start with a small MVP before full launch",
            "Test customer demand using surveys",
            "Focus on differentiation from competitors",
            "Control costs during the first three months"
        ],
        "final_recommendation": "Proceed With Improvements"
    }