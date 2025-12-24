# Problem: Maximal Rectangle
# Difficulty: Hard
# URL: https://leetcode.com/problems/maximal-rectangle/
# Runtime: 34 ms
# Memory: 23.7 MB

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
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