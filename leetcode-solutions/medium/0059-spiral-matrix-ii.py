# Problem: Spiral Matrix II
# Difficulty: Medium
# URL: https://leetcode.com/problems/spiral-matrix-ii/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1
        
        return matrix