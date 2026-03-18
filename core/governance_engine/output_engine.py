class GovernanceOutputEngine:

    def generate_output(self, scores, level, label, insights):
        """
        Generate structured governance report output
        """

        output = {
            "executive_summary": self._build_summary(level, label),
            "score_breakdown": scores,
            "risk_flags": self._identify_risks(scores),
            "recommendations": self._generate_recommendations(level)
        }

        return output


    def _build_summary(self, level, label):
        return f"Organization is at Level {level} ({label}) governance maturity."


    def _identify_risks(self, scores):
        risks = []

        if scores["policy_score"] < 60:
            risks.append("Weak policy framework")

        if scores["compliance_score"] < 60:
            risks.append("Compliance gaps detected")

        if scores["ethics_score"] < 60:
            risks.append("Ethical governance risk")

        if scores["decision_score"] < 60:
            risks.append("Decision-making inconsistency")

        return risks


    def _generate_recommendations(self, level):

        if level <= 2:
            return [
                "Establish formal governance structures",
                "Implement basic compliance controls",
                "Define policies and accountability"
            ]

        elif level == 3:
            return [
                "Standardize governance processes",
                "Improve monitoring and reporting",
                "Align governance with strategy"
            ]

        elif level == 4:
            return [
                "Integrate governance across departments",
                "Enhance risk management systems",
                "Automate compliance tracking"
            ]

        else:
            return [
                "Continuously optimize governance",
                "Leverage predictive risk analytics",
                "Benchmark against global best practices"
            ]
