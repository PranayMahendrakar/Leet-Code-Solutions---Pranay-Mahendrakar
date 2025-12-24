# Problem: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Runtime: 0 ms
# Memory: 13.2 MB

class Solution(object):
    def searchRange(self, nums, target):
        def findFirst():
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        def findLast():
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        return [findFirst(), findLast()]