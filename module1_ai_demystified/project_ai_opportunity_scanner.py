"""
Mini Project: AI Opportunity Scanner
Module 1 — AI Demystified (Week 4)
Sprint 1: Foundation

Scans business processes and identifies AI transformation opportunities.
"""
import json


def scan_opportunities(processes: list[dict]) -> list[dict]:
    """Score business processes for AI automation potential."""
    results = []
    for proc in processes:
        volume_score = min(proc.get("monthly_volume", 0) / 1000, 10)
        repetitive_score = proc.get("repetitiveness", 5)
        data_score = proc.get("data_availability", 5)
        error_rate = proc.get("current_error_rate", 0) * 10

        ai_score = round((volume_score + repetitive_score + data_score + error_rate) / 4, 1)
        priority = "HIGH" if ai_score >= 7 else "MEDIUM" if ai_score >= 4 else "LOW"

        savings_estimate = proc.get("monthly_cost", 0) * (proc.get("automation_potential", 0.5))
        annual_savings = round(savings_estimate * 12)

        results.append({
            "process": proc["name"],
            "ai_score": ai_score,
            "priority": priority,
            "estimated_annual_savings": f"${annual_savings:,}",
            "recommended_ai_type": classify_ai_type(proc),
        })

    return sorted(results, key=lambda x: -x["ai_score"])


def classify_ai_type(process: dict) -> str:
    """Recommend the type of AI solution for a business process."""
    if process.get("involves_text", False):
        return "Generative AI (LLM)"
    if process.get("involves_prediction", False):
        return "Predictive ML"
    if process.get("involves_images", False):
        return "Computer Vision"
    return "Process Automation (RPA + AI)"


if __name__ == "__main__":
    business_processes = [
        {"name": "Customer Email Triage", "monthly_volume": 15000, "repetitiveness": 9,
         "data_availability": 8, "current_error_rate": 0.15, "monthly_cost": 25000,
         "automation_potential": 0.7, "involves_text": True},
        {"name": "Invoice Processing", "monthly_volume": 5000, "repetitiveness": 10,
         "data_availability": 9, "current_error_rate": 0.08, "monthly_cost": 15000,
         "automation_potential": 0.8, "involves_images": True},
        {"name": "Sales Forecasting", "monthly_volume": 100, "repetitiveness": 6,
         "data_availability": 7, "current_error_rate": 0.25, "monthly_cost": 8000,
         "automation_potential": 0.6, "involves_prediction": True},
    ]

    results = scan_opportunities(business_processes)
    print("=== AI Opportunity Scanner Results ===\n")
    for r in results:
        print(f"{'🔴' if r['priority'] == 'HIGH' else '🟡' if r['priority'] == 'MEDIUM' else '🟢'} {r['process']}")
        print(f"   AI Score: {r['ai_score']}/10 | Priority: {r['priority']}")
        print(f"   Savings: {r['estimated_annual_savings']}/year")
        print(f"   Recommended: {r['recommended_ai_type']}")
        print()
