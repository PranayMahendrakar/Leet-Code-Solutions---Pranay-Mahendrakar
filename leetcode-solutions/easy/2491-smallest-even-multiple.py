# Problem: Smallest Even Multiple
# Difficulty: Easy
# URL: https://leetcode.com/problems/smallest-even-multiple/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def smallestEvenMultiple(self, n):
        return n if n % 2 == 0 else 2 * n