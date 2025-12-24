# Problem: Valid Parentheses
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-parentheses/
# Runtime: 4 ms
# Memory: 12.5 MB

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack