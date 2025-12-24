# Problem: Set Mismatch
# Difficulty: Easy
# URL: https://leetcode.com/problems/set-mismatch/
# Runtime: 3 ms
# Memory: 19.3 MB

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - sum(nums_set)
        duplicate = actual_sum - (expected_sum - missing)
        return [duplicate, missing]