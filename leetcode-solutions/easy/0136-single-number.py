# Problem: Single Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/single-number/
# Runtime: 3 ms
# Memory: 18.9 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result