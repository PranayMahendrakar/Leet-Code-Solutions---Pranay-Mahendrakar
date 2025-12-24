# Problem: Reshape the Matrix
# Difficulty: Easy
# URL: https://leetcode.com/problems/reshape-the-matrix/
# Runtime: 0 ms
# Memory: 17.9 MB

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [mat[i][j] for i in range(m) for j in range(n)]
        return [flat[i*c:(i+1)*c] for i in range(r)]