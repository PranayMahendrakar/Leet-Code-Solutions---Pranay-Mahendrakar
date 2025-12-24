# Problem: Subsets
# Difficulty: Medium
# URL: https://leetcode.com/problems/subsets/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result