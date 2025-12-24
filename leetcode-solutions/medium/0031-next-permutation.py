# Problem: Next Permutation
# Difficulty: Medium
# URL: https://leetcode.com/problems/next-permutation/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Find first decreasing element from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Find element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1