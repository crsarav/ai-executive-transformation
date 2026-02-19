"""
Capstone Project: AI Transformation Playbook
Module 6 — Change Management (Week 4)
Sprint 3: Launch

The final portfolio piece — a complete AI transformation framework
that combines everything learned across all 6 executive modules.
"""
import json


class AITransformationPlaybook:
    """
    Combines all executive skills from the 90-day sprint:
    - Module 1: AI understanding and landscape mapping
    - Module 2: Strategy and business case development
    - Module 3: Hands-on AI tool experience
    - Module 4: Team building and talent assessment
    - Module 5: Governance, risk, and ethics
    - Module 6: Change management and adoption
    """

    def __init__(self, org_name: str, industry: str, org_size: int):
        self.org_name = org_name
        self.industry = industry
        self.org_size = org_size
        self.phases = self._build_phases()

    def _build_phases(self) -> list[dict]:
        return [
            {
                "phase": 1,
                "name": "Discovery & Assessment",
                "duration": "4 weeks",
                "activities": [
                    "AI readiness assessment across all departments",
                    "Identify top 10 AI opportunities by business impact",
                    "Evaluate current data infrastructure",
                    "Benchmark against industry peers",
                ],
                "deliverables": ["AI Readiness Report", "Opportunity Matrix", "Data Audit"],
            },
            {
                "phase": 2,
                "name": "Strategy & Business Cases",
                "duration": "4 weeks",
                "activities": [
                    "Develop 3 priority AI business cases",
                    "Calculate ROI and build financial models",
                    "Define success metrics and KPIs",
                    "Present to executive committee for approval",
                ],
                "deliverables": ["AI Strategy Document", "Business Cases", "Board Presentation"],
            },
            {
                "phase": 3,
                "name": "Team & Infrastructure",
                "duration": "6 weeks",
                "activities": [
                    "Hire/assign AI team (ML engineers, data scientists)",
                    "Set up cloud ML platform",
                    "Establish AI governance framework",
                    "Launch AI training program for existing staff",
                ],
                "deliverables": ["Hiring Plan", "Platform Architecture", "Governance Charter"],
            },
            {
                "phase": 4,
                "name": "Pilot & Learn",
                "duration": "8 weeks",
                "activities": [
                    "Execute first AI pilot project",
                    "Measure against defined KPIs",
                    "Gather user feedback and iterate",
                    "Document lessons learned",
                ],
                "deliverables": ["Pilot Results Report", "Lessons Learned", "Scale Plan"],
            },
            {
                "phase": 5,
                "name": "Scale & Sustain",
                "duration": "Ongoing",
                "activities": [
                    "Scale successful pilots to production",
                    "Establish AI center of excellence",
                    "Continuous monitoring and improvement",
                    "Quarterly AI strategy reviews",
                ],
                "deliverables": ["Scale Roadmap", "CoE Charter", "Quarterly Reviews"],
            },
        ]

    def get_phase(self, phase_num: int) -> dict | None:
        return next((p for p in self.phases if p["phase"] == phase_num), None)

    def estimate_timeline(self) -> str:
        weeks = sum(int(p["duration"].split()[0]) for p in self.phases if "Ongoing" not in p["duration"])
        return f"{weeks} weeks to first production AI, then ongoing optimization"

    def estimate_investment(self) -> dict:
        base = self.org_size * 500
        return {
            "year_1_total": f"${base:,}",
            "talent": f"${int(base * 0.45):,}",
            "infrastructure": f"${int(base * 0.25):,}",
            "training": f"${int(base * 0.15):,}",
            "tools_vendors": f"${int(base * 0.15):,}",
        }

    def generate_executive_summary(self) -> str:
        investment = self.estimate_investment()
        return f"""
=== AI Transformation Playbook: {self.org_name} ===
Industry: {self.industry} | Size: {self.org_size} employees

Timeline: {self.estimate_timeline()}
Estimated Year 1 Investment: {investment['year_1_total']}

Phase Overview:
{chr(10).join(f"  Phase {p['phase']}: {p['name']} ({p['duration']})" for p in self.phases)}

Investment Breakdown:
  Talent: {investment['talent']}
  Infrastructure: {investment['infrastructure']}
  Training: {investment['training']}
  Tools & Vendors: {investment['tools_vendors']}
"""


if __name__ == "__main__":
    playbook = AITransformationPlaybook(
        org_name="Acme Corporation",
        industry="Financial Services",
        org_size=2000,
    )

    print(playbook.generate_executive_summary())

    print("\nDetailed Phase 1:")
    phase1 = playbook.get_phase(1)
    if phase1:
        print(f"  Activities:")
        for a in phase1["activities"]:
            print(f"    → {a}")
        print(f"  Deliverables: {', '.join(phase1['deliverables'])}")
