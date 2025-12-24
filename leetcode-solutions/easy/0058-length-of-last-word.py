# Problem: Length of Last Word
# Difficulty: Easy
# URL: https://leetcode.com/problems/length-of-last-word/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])