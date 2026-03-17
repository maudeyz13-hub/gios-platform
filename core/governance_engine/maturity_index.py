class GovernanceMaturityIndex:

    LEVELS = {
        1: "Reactive",
        2: "Basic",
        3: "Structured",
        4: "Integrated",
        5: "Optimized"
    }

    def __init__(self):
        self.score = 0

    def calculate_level(self, score):
        """
        Convert governance score into maturity level
        """

        if score < 20:
            return 1, self.LEVELS[1]

        elif score < 40:
            return 2, self.LEVELS[2]

        elif score < 60:
            return 3, self.LEVELS[3]

        elif score < 80:
            return 4, self.LEVELS[4]

        else:
            return 5, self.LEVELS[5]
