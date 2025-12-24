# Problem: Array Partition
# Difficulty: Easy
# URL: https://leetcode.com/problems/array-partition/
# Runtime: 35 ms
# Memory: 14.1 MB

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])