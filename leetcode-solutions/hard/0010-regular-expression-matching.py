# Problem: Regular Expression Matching
# Difficulty: Hard
# URL: https://leetcode.com/problems/regular-expression-matching/
# Runtime: 16 ms
# Memory: 12.6 MB

class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # dp[i][j] means s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Two cases:
                    # 1. Don't use the star (match zero occurrences)
                    dp[i][j] = dp[i][j - 2]
                    # 2. Use the star if current char matches
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]