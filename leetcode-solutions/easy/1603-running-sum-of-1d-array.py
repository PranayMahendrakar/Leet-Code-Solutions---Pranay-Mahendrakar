# Problem: Running Sum of 1d Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/running-sum-of-1d-array/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums