# Problem: Move Zeroes
# Difficulty: Easy
# URL: https://leetcode.com/problems/move-zeroes/
# Runtime: 9 ms
# Memory: 13.8 MB

class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1