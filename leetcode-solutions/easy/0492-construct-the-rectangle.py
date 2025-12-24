# Problem: Construct the Rectangle
# Difficulty: Easy
# URL: https://leetcode.com/problems/construct-the-rectangle/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def constructRectangle(self, area):
        import math
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]