class GovernanceAdvisoryEngine:

    def generate_advisory(self, scores, level, label, insights):
        """
        Generate executive-level governance advisory narrative
        """

        narrative = {
            "executive_brief": self._build_executive_brief(level, label),
            "risk_statement": self._build_risk_statement(insights),
            "strategic_position": self._build_positioning(level),
            "action_narrative": self._build_action_narrative(insights)
        }

        return narrative


    def _build_executive_brief(self, level, label):
        return f"The organization is currently operating at a {label} level of governance maturity (Level {level}), indicating its governance structures are {'underdeveloped' if level <= 2 else 'developing' if level == 3 else 'well-established' if level == 4 else 'highly optimized'}."


    def _build_risk_statement(self, insights):
        risk = insights["risk_level"]

        if risk == "HIGH RISK":
            return "The organization is exposed to significant governance and compliance risks that may impact strategic execution and regulatory standing."

        elif risk == "MEDIUM RISK":
            return "There are notable governance gaps that could affect operational consistency and risk management effectiveness."

        else:
            return "Governance structures are stable with manageable risk exposure, though continuous improvement is recommended."


    def _build_positioning(self, level):

        if level <= 2:
            return "Governance is largely reactive, with limited formalization and oversight."

        elif level == 3:
            return "Governance processes are defined but not consistently enforced across the organization."

        elif level == 4:
            return "Governance is integrated into operations and supports strategic alignment."

        else:
            return "Governance is optimized and continuously evolving, aligned with best-in-class standards."


    def _build_action_narrative(self, insights):

        actions = insights["priority_actions"]

        narrative = "Key priorities should focus on strengthening the following areas: "

        narrative += ", ".join(actions[:3])

        return narrative
