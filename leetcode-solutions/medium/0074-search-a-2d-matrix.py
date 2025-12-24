# Problem: Search a 2D Matrix
# Difficulty: Medium
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False