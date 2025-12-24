# Problem: Basic Calculator
# Difficulty: Hard
# URL: https://leetcode.com/problems/basic-calculator/
# Runtime: 118 ms
# Memory: 13.5 MB

class Solution(object):
    def calculate(self, s):
        result = 0
        num = 0
        sign = 1
        stack = []
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                result += sign * num
                num = 0
                sign = 1
            elif c == '-':
                result += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  # sign
                result += stack.pop()  # previous result
        
        return result + sign * num