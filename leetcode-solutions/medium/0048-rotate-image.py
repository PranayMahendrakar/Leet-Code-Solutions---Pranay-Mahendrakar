# Problem: Rotate Image
# Difficulty: Medium
# URL: https://leetcode.com/problems/rotate-image/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse rows
        for i in range(n):
            matrix[i].reverse()