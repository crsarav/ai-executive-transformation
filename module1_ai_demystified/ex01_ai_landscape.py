"""
Exercise 1: AI Landscape for Executives
Module 1 — AI Demystified
Sprint 1: Foundation (Day 1)

Task: Map the AI landscape relevant to your organization.
"""
import json


def map_ai_landscape() -> dict:
    """Map the current AI landscape from an executive perspective."""
    return {
        "generative_ai": {
            "description": "Creates new content (text, images, code)",
            "business_use": "Customer support, content creation, code assistance",
            "maturity": "production-ready",
            "key_vendors": ["OpenAI", "Anthropic", "Google", "Meta"],
            "typical_roi": "200-400%",
        },
        "predictive_ai": {
            "description": "Forecasts outcomes from historical data",
            "business_use": "Demand forecasting, churn prediction, fraud detection",
            "maturity": "mature",
            "key_vendors": ["AWS SageMaker", "Azure ML", "DataRobot"],
            "typical_roi": "300-600%",
        },
        "computer_vision": {
            "description": "Understands images and video",
            "business_use": "Quality inspection, security, document processing",
            "maturity": "production-ready",
            "key_vendors": ["Google Cloud Vision", "AWS Rekognition", "OpenCV"],
            "typical_roi": "150-350%",
        },
        "conversational_ai": {
            "description": "Natural language understanding and generation",
            "business_use": "Chatbots, virtual assistants, voice interfaces",
            "maturity": "production-ready",
            "key_vendors": ["OpenAI", "Google Dialogflow", "Amazon Lex"],
            "typical_roi": "250-500%",
        },
    }


if __name__ == "__main__":
    landscape = map_ai_landscape()
    print("=== AI Landscape for Executives ===\n")
    for category, details in landscape.items():
        print(f"📌 {category.replace('_', ' ').title()}")
        print(f"   What: {details['description']}")
        print(f"   Business use: {details['business_use']}")
        print(f"   Maturity: {details['maturity']}")
        print(f"   Typical ROI: {details['typical_roi']}")
        print()
