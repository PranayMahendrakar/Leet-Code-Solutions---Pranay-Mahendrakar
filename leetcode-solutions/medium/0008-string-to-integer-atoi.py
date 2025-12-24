# Problem: String to Integer (atoi)
# Difficulty: Medium
# URL: https://leetcode.com/problems/string-to-integer-atoi/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result