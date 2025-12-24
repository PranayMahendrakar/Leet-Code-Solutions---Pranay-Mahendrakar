# Problem: Largest Number At Least Twice of Others
# Difficulty: Easy
# URL: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# Runtime: 3 ms
# Memory: 12.5 MB

class Solution(object):
    def dominantIndex(self, nums):
        max_val = max(nums)
        max_idx = nums.index(max_val)
        for num in nums:
            if num != max_val and max_val < 2 * num:
                return -1
        return max_idx