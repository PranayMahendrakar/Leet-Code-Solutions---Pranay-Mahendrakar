# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime: 167 ms
# Memory: 32.1 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        