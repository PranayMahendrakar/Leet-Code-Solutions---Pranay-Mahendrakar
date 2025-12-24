# Problem: Baseball Game
# Difficulty: Easy
# URL: https://leetcode.com/problems/baseball-game/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)