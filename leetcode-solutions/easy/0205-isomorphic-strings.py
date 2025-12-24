# Problem: Isomorphic Strings
# Difficulty: Easy
# URL: https://leetcode.com/problems/isomorphic-strings/
# Runtime: 3 ms
# Memory: 15.1 MB

class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))