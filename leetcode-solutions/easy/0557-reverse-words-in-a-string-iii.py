# Problem: Reverse Words in a String III
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Runtime: 3 ms
# Memory: 13 MB

class Solution(object):
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split())