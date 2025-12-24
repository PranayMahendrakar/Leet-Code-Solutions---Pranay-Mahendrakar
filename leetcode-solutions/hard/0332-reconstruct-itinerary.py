# Problem: Reconstruct Itinerary
# Difficulty: Hard
# URL: https://leetcode.com/problems/reconstruct-itinerary/
# Runtime: 3 ms
# Memory: 12.9 MB

class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        
        # Build adjacency list with sorted destinations (reverse for pop efficiency)
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        route = []
        
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)
        
        dfs("JFK")
        return route[::-1]