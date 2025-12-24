# Problem: Gray Code
# Difficulty: Medium
# URL: https://leetcode.com/problems/gray-code/
# Runtime: 3 ms
# Memory: 18.9 MB

class Solution:
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            result += [x + (1 << i) for x in reversed(result)]
        return result