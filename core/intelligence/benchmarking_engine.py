class GovernanceBenchmarkingEngine:

    def benchmark(self, scores, peer_data):
        """
        Compare company scores against peer dataset
        """

        benchmark_result = {
            "peer_average": self._calculate_peer_average(peer_data),
            "positioning": self._calculate_position(scores, peer_data),
            "top_performers": self._identify_top_performers(peer_data)
        }

        return benchmark_result


    def _calculate_peer_average(self, peer_data):

        total = sum([p["final_score"] for p in peer_data])
        avg = total / len(peer_data)

        return round(avg, 2)


    def _calculate_position(self, scores, peer_data):

        lower_count = sum(1 for p in peer_data if p["final_score"] < scores["final_score"])
        percentile = (lower_count / len(peer_data)) * 100

        return f"{round(percentile)}th percentile"


    def _identify_top_performers(self, peer_data):

        sorted_peers = sorted(peer_data, key=lambda x: x["final_score"], reverse=True)

        return sorted_peers[:3]
