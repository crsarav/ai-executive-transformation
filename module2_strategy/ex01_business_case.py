"""
Exercise 1: AI Business Case Builder
Module 2 — Strategy & Business Cases
Sprint 1: Foundation

Task: Create a function called build_business_case that generates
a structured AI business case for board presentation.
"""
import json


def build_business_case(
    project_name: str,
    problem: str,
    ai_solution: str,
    investment: float,
    expected_benefit: float,
    timeline_months: int,
    risks: list[str],
) -> dict:
    """Build a structured AI business case."""
    roi = round(((expected_benefit * 3) - investment) / investment * 100, 1)

    return {
        "executive_summary": f"Invest ${investment:,.0f} in {project_name} to {problem.lower()}. "
                             f"Expected 3-year ROI: {roi}%.",
        "project_name": project_name,
        "problem_statement": problem,
        "proposed_solution": ai_solution,
        "financials": {
            "upfront_investment": f"${investment:,.0f}",
            "annual_benefit": f"${expected_benefit:,.0f}",
            "3_year_roi": f"{roi}%",
            "payback_period": f"{round(investment / (expected_benefit / 12))} months",
        },
        "timeline": f"{timeline_months} months to production",
        "key_risks": risks,
        "recommendation": "APPROVE" if roi > 150 else "CONDITIONAL" if roi > 50 else "DEFER",
        "next_steps": [
            "Secure budget approval",
            f"Assemble team (estimated {max(3, timeline_months // 2)} people)",
            "Begin vendor evaluation",
            "Set up data pipeline",
        ],
    }


if __name__ == "__main__":
    case = build_business_case(
        project_name="AI-Powered Customer Support",
        problem="Reduce average ticket resolution time from 4 hours to 15 minutes",
        ai_solution="Deploy LLM-based agent that auto-resolves L1 tickets and assists L2 agents",
        investment=350000,
        expected_benefit=500000,
        timeline_months=6,
        risks=["Data quality issues", "Change resistance from support team", "AI hallucination risk"],
    )
    print(json.dumps(case, indent=2))
