def benchmark(self, scores, peer_data):
    """
    Intelligent benchmarking against peer dataset
    """

    peer_average = self._calculate_peer_average(peer_data)
    percentile = self._calculate_percentile(scores, peer_data)
    positioning = self._determine_position(percentile)
    top_performers = self._identify_top_performers(peer_data)
    narrative = self._generate_narrative(percentile)

    return {
        "peer_average": peer_average,
        "percentile": percentile,
        "positioning": positioning,
        "top_performers": top_performers,
        "narrative": narrative
    }
def _calculate_percentile(self, scores, peer_data):
    lower_count = sum(
        1 for p in peer_data
        if p["final_score"] < scores["final_score"]
    )

    percentile = (lower_count / len(peer_data)) * 100
    return round(percentile)

def _determine_position(self, percentile):
    if percentile < 40:
        return "Below Average"
    elif percentile < 70:
        return "Average"
    else:
        return "Above Average"

def _generate_narrative(self, percentile):
    return f"Your organization outperforms {percentile}% of comparable organizations."
