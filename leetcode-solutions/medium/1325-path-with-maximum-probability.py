# Problem: Path with Maximum Probability
# Difficulty: Medium
# URL: https://leetcode.com/problems/path-with-maximum-probability/
# Runtime: 90 ms
# Memory: 27.9 MB

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        import heapq
        from collections import defaultdict
        
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        prob = [0.0] * n
        prob[start_node] = 1.0
        
        # Max heap (use negative for max)
        heap = [(-1.0, start_node)]
        
        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob
            
            if node == end_node:
                return curr_prob
            
            if curr_prob < prob[node]:
                continue
                
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        
        return 0.0