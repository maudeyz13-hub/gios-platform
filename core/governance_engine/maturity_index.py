from core.governance_engine.scoring_engine import GovernanceScoringEngine
from core.governance_engine.maturity_index import GovernanceMaturityIndex

# Initialize engines
scoring_engine = GovernanceScoringEngine()
maturity_engine = GovernanceMaturityIndex()

# Sample input
sample_input = {
    "policies": [{"score": 60}, {"score": 80}],
    "compliance": [{"score": 70}, {"score": 75}],
    "ethics": [{"score": 65}, {"score": 85}],
    "decisions": [{"score": 50}, {"score": 90}]
}

# Step 1: Calculate scores
scores = scoring_engine.calculate_scores(sample_input)

# Step 2: Convert to maturity
level, label = maturity_engine.calculate_level(scores["final_score"])

print("Scores:", scores)
print("Maturity Level:", level, "-", label)
