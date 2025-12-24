# Problem: Longest Continuous Increasing Subsequence
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Runtime: 1 ms
# Memory: 18.6 MB

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
        return max_len