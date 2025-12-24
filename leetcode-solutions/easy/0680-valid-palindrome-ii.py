# Problem: Valid Palindrome II
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-palindrome-ii/
# Runtime: 90 ms
# Memory: 12.6 MB

class Solution(object):
    def validPalindrome(self, s):
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l+1, r) or is_palindrome(l, r-1)
            l += 1
            r -= 1
        return True