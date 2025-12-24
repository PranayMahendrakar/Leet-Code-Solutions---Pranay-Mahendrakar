# Problem: Container With Most Water
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/
# Runtime: 126 ms
# Memory: 20.7 MB

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area