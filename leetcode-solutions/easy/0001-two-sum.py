# Problem: Two Sum
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Runtime: 0 ms
# Memory: 13.2 MB

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i