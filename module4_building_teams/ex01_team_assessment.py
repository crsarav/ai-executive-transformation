"""
Exercise 1: AI Team Readiness Assessment
Module 4 — Building AI Teams
Sprint 2: Build

Task: Create a function called assess_ai_readiness that evaluates
an organization's readiness to build AI capabilities.
"""
import json


def assess_ai_readiness(
    data_maturity: int,
    talent: int,
    infrastructure: int,
    governance: int,
    culture: int,
) -> dict:
    """Assess organizational AI readiness across 5 dimensions (1-10 scale)."""
    dimensions = {
        "data_maturity": {"score": data_maturity, "weight": 0.25},
        "talent": {"score": talent, "weight": 0.25},
        "infrastructure": {"score": infrastructure, "weight": 0.20},
        "governance": {"score": governance, "weight": 0.15},
        "culture": {"score": culture, "weight": 0.15},
    }

    overall = sum(d["score"] * d["weight"] for d in dimensions.values())

    gaps = [name for name, d in dimensions.items() if d["score"] < 5]
    strengths = [name for name, d in dimensions.items() if d["score"] >= 7]

    if overall >= 7:
        stage = "AI-Ready"
        recommendation = "Begin production AI projects immediately"
    elif overall >= 5:
        stage = "AI-Developing"
        recommendation = "Invest in gaps before scaling AI initiatives"
    else:
        stage = "AI-Early"
        recommendation = "Start with awareness, training, and data foundation"

    return {
        "overall_score": round(overall, 1),
        "stage": stage,
        "recommendation": recommendation,
        "dimensions": {k: v["score"] for k, v in dimensions.items()},
        "strengths": strengths,
        "gaps": gaps,
        "priority_actions": generate_actions(gaps),
    }


def generate_actions(gaps: list[str]) -> list[str]:
    """Generate priority actions based on identified gaps."""
    actions_map = {
        "data_maturity": "Implement data quality framework and central data catalog",
        "talent": "Hire ML engineers and upskill existing developers in AI",
        "infrastructure": "Set up cloud ML platform (AWS SageMaker / Azure ML)",
        "governance": "Establish AI ethics board and model risk framework",
        "culture": "Run AI awareness workshops and identify internal champions",
    }
    return [actions_map[gap] for gap in gaps if gap in actions_map]


if __name__ == "__main__":
    result = assess_ai_readiness(
        data_maturity=7, talent=5, infrastructure=8, governance=4, culture=6
    )
    print("=== AI Readiness Assessment ===\n")
    print(f"Overall Score: {result['overall_score']}/10")
    print(f"Stage: {result['stage']}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"\nStrengths: {', '.join(result['strengths']) or 'None'}")
    print(f"Gaps: {', '.join(result['gaps']) or 'None'}")
    print(f"\nPriority Actions:")
    for action in result['priority_actions']:
        print(f"  → {action}")
