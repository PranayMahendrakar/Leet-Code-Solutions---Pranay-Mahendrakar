# Problem: Binary Search
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-search/
# Runtime: 0 ms
# Memory: 18.4 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1