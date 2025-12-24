# Problem: Number of Common Factors
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-common-factors/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def commonFactors(self, a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        g = gcd(a, b)
        count = 0
        for i in range(1, g + 1):
            if g % i == 0:
                count += 1
        return count