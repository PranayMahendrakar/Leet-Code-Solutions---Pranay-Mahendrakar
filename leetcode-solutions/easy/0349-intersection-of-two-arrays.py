# Problem: Intersection of Two Arrays
# Difficulty: Easy
# URL: https://leetcode.com/problems/intersection-of-two-arrays/
# Runtime: 0 ms
# Memory: 17.3 MB

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))