"""
Exercise 1: AI Risk Assessment Framework
Module 5 — Governance & Ethics
Sprint 3: Launch

Task: Build an AI risk scoring system for governance review.
"""
import json


def assess_ai_risk(
    model_type: str,
    data_sensitivity: str,
    decision_impact: str,
    human_oversight: bool,
    bias_tested: bool,
) -> dict:
    """Score AI project risk for governance approval."""
    sensitivity_scores = {"public": 1, "internal": 3, "confidential": 7, "pii": 9}
    impact_scores = {"informational": 1, "operational": 4, "financial": 7, "safety": 10}

    data_score = sensitivity_scores.get(data_sensitivity, 5)
    impact_score = impact_scores.get(decision_impact, 5)
    oversight_reduction = -2 if human_oversight else 0
    bias_reduction = -1 if bias_tested else 1

    risk_score = max(1, min(10, round((data_score + impact_score) / 2 + oversight_reduction + bias_reduction)))

    risk_level = "HIGH" if risk_score >= 7 else "MEDIUM" if risk_score >= 4 else "LOW"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "approval_required": "Board" if risk_level == "HIGH" else "VP" if risk_level == "MEDIUM" else "Manager",
        "mitigations_required": get_mitigations(risk_level, human_oversight, bias_tested),
        "review_frequency": "Monthly" if risk_level == "HIGH" else "Quarterly",
    }


def get_mitigations(risk_level: str, has_oversight: bool, has_bias_test: bool) -> list[str]:
    mitigations = []
    if not has_oversight:
        mitigations.append("Add human-in-the-loop review")
    if not has_bias_test:
        mitigations.append("Conduct bias and fairness audit")
    if risk_level in ["HIGH", "MEDIUM"]:
        mitigations.append("Implement model monitoring and drift detection")
        mitigations.append("Document model cards and decision explanations")
    if risk_level == "HIGH":
        mitigations.append("Establish incident response plan for AI failures")
    return mitigations


if __name__ == "__main__":
    projects = [
        {"name": "Email Auto-Reply", "model": "LLM", "data": "internal", "impact": "operational", "oversight": True, "bias": True},
        {"name": "Loan Approval AI", "model": "ML Classifier", "data": "pii", "impact": "financial", "oversight": False, "bias": False},
        {"name": "Meeting Summarizer", "model": "LLM", "data": "confidential", "impact": "informational", "oversight": True, "bias": True},
    ]

    print("=== AI Risk Assessment ===\n")
    for p in projects:
        result = assess_ai_risk(p["model"], p["data"], p["impact"], p["oversight"], p["bias"])
        print(f"{'🔴' if result['risk_level'] == 'HIGH' else '🟡' if result['risk_level'] == 'MEDIUM' else '🟢'} {p['name']}")
        print(f"   Risk: {result['risk_score']}/10 ({result['risk_level']})")
        print(f"   Approval: {result['approval_required']}")
        print(f"   Review: {result['review_frequency']}")
        if result['mitigations_required']:
            print(f"   Mitigations:")
            for m in result['mitigations_required']:
                print(f"     → {m}")
        print()
