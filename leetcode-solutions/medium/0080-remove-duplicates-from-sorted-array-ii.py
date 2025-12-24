# Problem: Remove Duplicates from Sorted Array II
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Runtime: 75 ms
# Memory: 15.3 MB

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        write = 2
        
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write