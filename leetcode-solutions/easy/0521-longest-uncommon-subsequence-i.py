# Problem: Longest Uncommon Subsequence I
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Runtime: 0 ms
# Memory: 12.3 MB

class Solution(object):
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))