# Problem: Power of Three
# Difficulty: Easy
# URL: https://leetcode.com/problems/power-of-three/
# Runtime: 16 ms
# Memory: 17.6 MB

class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0