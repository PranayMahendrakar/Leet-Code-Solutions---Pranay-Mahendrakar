# Problem: Intersection of Two Arrays II
# Difficulty: Easy
# URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Runtime: 4 ms
# Memory: 12.6 MB

class Solution(object):
    def intersect(self, nums1, nums2):
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        return list((c1 & c2).elements())