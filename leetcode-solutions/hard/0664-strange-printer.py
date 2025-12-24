# Problem: Strange Printer
# Difficulty: Hard
# URL: https://leetcode.com/problems/strange-printer/
# Runtime: 347 ms
# Memory: 12.6 MB

class Solution:
    def strangePrinter(self, s):
        # Remove consecutive duplicates
        s = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i-1])
        n = len(s)
        if n == 0:
            return 0
        
        # dp[i][j] = min turns to print s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1
        
        # Fill DP table for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Worst case: print s[i] separately
                dp[i][j] = dp[i + 1][j] + 1
                
                # Try to merge with matching characters
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        cost = dp[i + 1][k - 1] if k > i + 1 else 0
                        cost += dp[k][j]
                        dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n - 1]