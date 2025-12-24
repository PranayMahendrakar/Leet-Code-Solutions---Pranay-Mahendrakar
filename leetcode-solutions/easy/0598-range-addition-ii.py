# Problem: Range Addition II
# Difficulty: Easy
# URL: https://leetcode.com/problems/range-addition-ii/
# Runtime: 0 ms
# Memory: 13.4 MB

class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        min_row = min(op[0] for op in ops)
        min_col = min(op[1] for op in ops)
        return min_row * min_col