# Problem: Unique Paths
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-paths/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]