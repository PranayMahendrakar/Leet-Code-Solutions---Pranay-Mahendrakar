# Problem: Remove Duplicates from Sorted Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Runtime: 4 ms
# Memory: 14.1 MB

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1  # Position for next unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k