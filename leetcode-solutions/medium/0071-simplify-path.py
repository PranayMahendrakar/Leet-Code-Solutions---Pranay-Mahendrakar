# Problem: Simplify Path
# Difficulty: Medium
# URL: https://leetcode.com/problems/simplify-path/
# Runtime: 3 ms
# Memory: 12.6 MB

class Solution:
    def simplifyPath(self, path):
        stack = []
        for part in path.split('/'):
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)