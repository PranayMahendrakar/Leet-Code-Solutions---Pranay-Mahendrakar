# Problem: Next Greater Element I
# Difficulty: Easy
# URL: https://leetcode.com/problems/next-greater-element-i/
# Runtime: 1 ms
# Memory: 12.8 MB

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nge = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num
            stack.append(num)
        return [nge.get(num, -1) for num in nums1]