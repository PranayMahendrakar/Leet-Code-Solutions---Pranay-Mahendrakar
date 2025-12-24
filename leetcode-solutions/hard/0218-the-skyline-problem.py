# Problem: The Skyline Problem
# Difficulty: Hard
# URL: https://leetcode.com/problems/the-skyline-problem/
# Runtime: 43 ms
# Memory: 21.3 MB

class Solution(object):
    def getSkyline(self, buildings):
        import heapq
        
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # start
            events.append((right, 0, 0))  # end
        
        events.sort()
        
        result = [[0, 0]]
        heap = [(0, float('inf'))]  # (neg_height, end)
        
        for x, neg_h, end in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            if neg_h:  # start event
                heapq.heappush(heap, (neg_h, end))
            
            max_h = -heap[0][0]
            if result[-1][1] != max_h:
                result.append([x, max_h])
        
        return result[1:]