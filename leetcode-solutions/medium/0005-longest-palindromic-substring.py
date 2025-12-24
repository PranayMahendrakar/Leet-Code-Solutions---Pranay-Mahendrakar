# Problem: Longest Palindromic Substring
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-palindromic-substring/
# Runtime: 362 ms
# Memory: 12.7 MB

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        result = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expand(i, i)
            if len(odd) > len(result):
                result = odd
            # Even length palindrome
            even = expand(i, i + 1)
            if len(even) > len(result):
                result = even
        
        return result