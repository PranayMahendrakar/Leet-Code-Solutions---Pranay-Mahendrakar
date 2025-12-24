# Problem: Find Minimum in Rotated Sorted Array II
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Runtime: 4 ms
# Memory: 12.8 MB

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is in left half (including mid)
                right = mid
            else:
                # nums[mid] == nums[right], can't determine, shrink right
                right -= 1
        
        return nums[left]