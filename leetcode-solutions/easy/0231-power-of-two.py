# Problem: Power of Two
# Difficulty: Easy
# URL: https://leetcode.com/problems/power-of-two/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0