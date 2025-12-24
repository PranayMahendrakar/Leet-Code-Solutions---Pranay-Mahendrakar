# Problem: Longest Palindrome
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-palindrome/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def longestPalindrome(self, s):
        from collections import Counter
        count = Counter(s)
        length = 0
        odd_found = False
        for c in count.values():
            length += c // 2 * 2
            if c % 2 == 1:
                odd_found = True
        return length + 1 if odd_found else length