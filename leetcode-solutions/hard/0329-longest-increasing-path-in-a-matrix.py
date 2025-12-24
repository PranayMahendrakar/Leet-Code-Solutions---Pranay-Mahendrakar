# Problem: Longest Increasing Path in a Matrix
# Difficulty: Hard
# URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Runtime: 167 ms
# Memory: 22.3 MB

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    result = max(result, 1 + dfs(ni, nj))
            
            memo[(i, j)] = result
            return result
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans