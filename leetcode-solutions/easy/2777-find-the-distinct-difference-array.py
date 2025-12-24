# Problem: Find the Distinct Difference Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-the-distinct-difference-array/
# Runtime: 23 ms
# Memory: 12.5 MB

class Solution(object):
    def distinctDifferenceArray(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            result.append(prefix - suffix)
        return result