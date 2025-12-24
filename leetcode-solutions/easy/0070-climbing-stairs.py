# Problem: Climbing Stairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/climbing-stairs/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a