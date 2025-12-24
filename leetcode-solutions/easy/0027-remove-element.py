# Problem: Remove Element
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-element/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Position for next valid element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k