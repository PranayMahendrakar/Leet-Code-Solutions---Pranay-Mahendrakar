# Problem: Missing Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/missing-number/
# Runtime: 0 ms
# Memory: 13.5 MB

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)