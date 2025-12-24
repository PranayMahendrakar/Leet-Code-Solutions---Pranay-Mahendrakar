# Problem: Add Digits
# Difficulty: Easy
# URL: https://leetcode.com/problems/add-digits/
# Runtime: 1 ms
# Memory: 12.5 MB

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + (num - 1) % 9