# Problem: Find the Difference
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-the-difference/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)