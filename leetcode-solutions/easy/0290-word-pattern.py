# Problem: Word Pattern
# Difficulty: Easy
# URL: https://leetcode.com/problems/word-pattern/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        return len(pattern) == len(words) and len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))