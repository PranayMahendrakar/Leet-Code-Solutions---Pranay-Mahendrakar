# Problem: First Unique Character in a String
# Difficulty: Easy
# URL: https://leetcode.com/problems/first-unique-character-in-a-string/
# Runtime: 166 ms
# Memory: 12.6 MB

class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1