# Problem: IPO
# Difficulty: Hard
# URL: https://leetcode.com/problems/ipo/
# Runtime: 929 ms
# Memory: 36.4 MB

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        import heapq
        
        n = len(profits)
        # Create list of (capital, profit) pairs, sorted by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []  # Max heap of available profits (stored as negatives)
        i = 0
        
        for _ in range(k):
            # Add all projects that can be started with current capital
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no project can be started, break
            if not max_heap:
                break
            
            # Take the most profitable project
            w -= heapq.heappop(max_heap)  # Subtract negative = add positive
        
        return w