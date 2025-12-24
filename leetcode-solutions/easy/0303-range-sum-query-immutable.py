# Problem: Range Sum Query - Immutable
# Difficulty: Easy
# URL: https://leetcode.com/problems/range-sum-query-immutable/
# Runtime: 7 ms
# Memory: 16.1 MB

class NumArray(object):
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]