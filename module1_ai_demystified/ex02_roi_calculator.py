"""
Exercise 2: AI ROI Calculator
Module 1 — AI Demystified
Sprint 1: Foundation (Day 2)

Task: Calculate the ROI of an AI investment for board presentation.
"""


def calculate_ai_roi(
    investment: float,
    annual_savings: float,
    revenue_increase: float,
    implementation_months: int = 6,
    years: int = 3,
) -> dict:
    """Calculate comprehensive AI ROI for executive decision-making."""
    total_benefit = (annual_savings + revenue_increase) * years
    net_benefit = total_benefit - investment
    roi_percent = (net_benefit / investment) * 100
    payback_months = round(investment / ((annual_savings + revenue_increase) / 12))
    monthly_benefit = (annual_savings + revenue_increase) / 12

    return {
        "investment": f"${investment:,.0f}",
        "annual_benefit": f"${annual_savings + revenue_increase:,.0f}",
        "3_year_total_benefit": f"${total_benefit:,.0f}",
        "net_benefit": f"${net_benefit:,.0f}",
        "roi_percent": f"{roi_percent:.1f}%",
        "payback_months": payback_months,
        "monthly_benefit_after_payback": f"${monthly_benefit:,.0f}",
        "recommendation": "APPROVE" if roi_percent > 100 else "REVIEW" if roi_percent > 50 else "DEFER",
    }


if __name__ == "__main__":
    projects = [
        {"name": "Customer Support AI", "investment": 200000, "annual_savings": 150000, "revenue_increase": 50000},
        {"name": "Predictive Maintenance", "investment": 500000, "annual_savings": 300000, "revenue_increase": 100000},
        {"name": "AI Content Generation", "investment": 50000, "annual_savings": 80000, "revenue_increase": 30000},
    ]

    print("=== AI Investment ROI Analysis ===\n")
    for p in projects:
        roi = calculate_ai_roi(p["investment"], p["annual_savings"], p["revenue_increase"])
        print(f"📊 {p['name']}")
        for k, v in roi.items():
            print(f"   {k}: {v}")
        print()
