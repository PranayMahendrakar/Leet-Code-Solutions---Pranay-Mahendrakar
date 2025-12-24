# Problem: Ransom Note
# Difficulty: Easy
# URL: https://leetcode.com/problems/ransom-note/
# Runtime: 53 ms
# Memory: 12.8 MB

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        return not (Counter(ransomNote) - Counter(magazine))