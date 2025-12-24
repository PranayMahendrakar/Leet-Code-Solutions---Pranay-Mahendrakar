# Problem: Longest Increasing Subsequence
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-increasing-subsequence/
# Runtime: 3 ms
# Memory: 17.7 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
        