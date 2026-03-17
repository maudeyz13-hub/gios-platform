from core.governance_engine.output_engine import GovernanceOutputEngine
from core.governance_engine.scoring_engine import GovernanceScoringEngine
from core.governance_engine.maturity_index import GovernanceMaturityIndex

# Initialize engines
scoring_engine = GovernanceScoringEngine()
maturity_engine = GovernanceMaturityIndex()
output_engine = GovernanceOutputEngine()

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

# Step 3: Generate output
report = output_engine.generate_output(scores, level, label)

print("Scores:", scores)
print("Maturity Level:", level, "-", label)
print("FINAL REPORT:")
print(report)
