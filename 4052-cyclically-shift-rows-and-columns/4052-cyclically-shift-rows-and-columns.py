class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        """
        :type n: int
        :type grid: List[List[int]]
        :type rowShift: List[int]
        :type colShift: List[int]
        :rtype: List[List[int]]
        """
        rows = [grid[i][rowShift[i]:] + grid[i][:rowShift[i]] for i in range(n)]
        return [[rows[(i + colShift[j]) % n][j] for j in range(n)] for i in range(n)]