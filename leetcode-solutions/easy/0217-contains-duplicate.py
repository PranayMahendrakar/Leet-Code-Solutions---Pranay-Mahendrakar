# Problem: Contains Duplicate
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Runtime: 13 ms
# Memory: 26.1 MB

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))