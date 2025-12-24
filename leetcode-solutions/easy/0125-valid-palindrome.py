# Problem: Valid Palindrome
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-palindrome/
# Runtime: 7 ms
# Memory: 22.5 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter only alphanumeric characters and convert to lowercase
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]