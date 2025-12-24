# Problem: Combinations
# Difficulty: Medium
# URL: https://leetcode.com/problems/combinations/
# Runtime: 259 ms
# Memory: 131.4 MB

class Solution:
    def combine(self, n, k):
        result = []
        
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return result