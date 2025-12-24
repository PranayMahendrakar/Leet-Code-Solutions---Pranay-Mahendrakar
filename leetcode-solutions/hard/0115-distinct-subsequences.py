# Problem: Distinct Subsequences
# Difficulty: Hard
# URL: https://leetcode.com/problems/distinct-subsequences/
# Runtime: 643 ms
# Memory: 69.5 MB

class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[m][n]