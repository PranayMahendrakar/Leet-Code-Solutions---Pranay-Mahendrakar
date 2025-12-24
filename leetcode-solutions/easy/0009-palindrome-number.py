# Problem: Palindrome Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome-number/
# Runtime: 16 ms
# Memory: 12.5 MB

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]