# Problem: Largest Rectangle in Histogram
# Difficulty: Hard
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Runtime: 196 ms
# Memory: 28.4 MB

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))
        
        return max_area