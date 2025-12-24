# Problem: Ugly Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/ugly-number/
# Runtime: 0 ms
# Memory: 12.3 MB

class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1