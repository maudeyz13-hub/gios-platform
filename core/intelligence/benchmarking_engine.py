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
