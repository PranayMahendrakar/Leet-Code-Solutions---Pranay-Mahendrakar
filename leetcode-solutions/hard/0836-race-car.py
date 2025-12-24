# Problem: Race Car
# Difficulty: Hard
# URL: https://leetcode.com/problems/race-car/
# Runtime: 92 ms
# Memory: 12.9 MB

class Solution:
    def racecar(self, target):
        dp = [0] * (target + 1)
        
        for t in range(1, target + 1):
            # Find the minimum n where 2^n - 1 >= t
            n = t.bit_length()
            
            # If we can reach exactly with n A's
            if (1 << n) - 1 == t:
                dp[t] = n
                continue
            
            # Option 1: Go past target, then reverse
            dp[t] = n + 1 + dp[(1 << n) - 1 - t]
            
            # Option 2: Go less, reverse, go back some, reverse again
            for m in range(n - 1):
                go = (1 << (n - 1)) - 1  # n-1 A's
                back = (1 << m) - 1      # m A's
                remaining = t - go + back
                # Cost: (n-1) A's + R + m A's + R + dp[remaining]
                dp[t] = min(dp[t], (n - 1) + 1 + m + 1 + dp[remaining])
        
        return dp[target]