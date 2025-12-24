# Problem: Base 7
# Difficulty: Easy
# URL: https://leetcode.com/problems/base-7/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        result = ""
        while num:
            result = str(num % 7) + result
            num //= 7
        return "-" + result if negative else result