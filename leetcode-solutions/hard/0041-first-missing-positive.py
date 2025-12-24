# Problem: First Missing Positive
# Difficulty: Hard
# URL: https://leetcode.com/problems/first-missing-positive/
# Runtime: 69 ms
# Memory: 20.2 MB

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Place each number in its correct position
        # nums[i] should be i+1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Find first position where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1