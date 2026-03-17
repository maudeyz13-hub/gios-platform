class GovernanceIntelligenceEngine:

    def analyze(self, scores):
        """
        Perform advanced governance intelligence analysis
        """

        insights = {
            "weak_areas": self._detect_weaknesses(scores),
            "risk_level": self._calculate_risk_level(scores),
            "priority_actions": self._prioritize_actions(scores)
        }

        return insights


    def _detect_weaknesses(self, scores):
        weaknesses = []

        if scores["policy_score"] < 60:
            weaknesses.append("Policy framework is underdeveloped")

        if scores["compliance_score"] < 60:
            weaknesses.append("Compliance exposure risk")

        if scores["ethics_score"] < 60:
            weaknesses.append("Ethical governance gaps")

        if scores["decision_score"] < 60:
            weaknesses.append("Decision inconsistency risk")

        return weaknesses


    def _calculate_risk_level(self, scores):

        final_score = scores["final_score"]

        if final_score < 40:
            return "HIGH RISK"

        elif final_score < 70:
            return "MEDIUM RISK"

        else:
            return "LOW RISK"


    def _prioritize_actions(self, scores):

        priorities = []

        sorted_scores = sorted(
            [
                ("policy", scores["policy_score"]),
                ("compliance", scores["compliance_score"]),
                ("ethics", scores["ethics_score"]),
                ("decision", scores["decision_score"])
            ],
            key=lambda x: x[1]
        )

        for area, score in sorted_scores:
            priorities.append(f"Improve {area} governance (score: {score})")

        return priorities
