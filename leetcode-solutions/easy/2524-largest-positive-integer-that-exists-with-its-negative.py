# Problem: Largest Positive Integer That Exists With Its Negative
# Difficulty: Easy
# URL: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Runtime: 10 ms
# Memory: 12.7 MB

class Solution(object):
    def findMaxK(self, nums):
        num_set = set(nums)
        result = -1
        for num in nums:
            if num > 0 and -num in num_set:
                result = max(result, num)
        return result