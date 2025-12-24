# Problem: Detect Capital
# Difficulty: Easy
# URL: https://leetcode.com/problems/detect-capital/
# Runtime: 0 ms
# Memory: 12.3 MB

class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())