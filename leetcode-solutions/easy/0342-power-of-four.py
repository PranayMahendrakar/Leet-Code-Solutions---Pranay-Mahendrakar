# Problem: Power of Four
# Difficulty: Easy
# URL: https://leetcode.com/problems/power-of-four/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0