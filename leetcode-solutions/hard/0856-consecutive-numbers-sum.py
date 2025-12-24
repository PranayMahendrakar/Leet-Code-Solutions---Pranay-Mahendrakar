# Problem: Consecutive Numbers Sum
# Difficulty: Hard
# URL: https://leetcode.com/problems/consecutive-numbers-sum/
# Runtime: 95 ms
# Memory: 12.4 MB

class Solution:
    def consecutiveNumbersSum(self, n):
        # Sum of k consecutive numbers starting from x: k*x + k*(k-1)/2 = n
        # k*x = n - k*(k-1)/2
        # x must be positive integer
        
        count = 0
        k = 1
        
        while k * (k - 1) // 2 < n:
            remainder = n - k * (k - 1) // 2
            if remainder % k == 0:
                count += 1
            k += 1
        
        return count