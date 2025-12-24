# Problem: Pascal's Triangle II
# Difficulty: Easy
# URL: https://leetcode.com/problems/pascals-triangle-ii/
# Runtime: 3 ms
# Memory: 12.3 MB

class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex + 1):
            # Build row from right to left to avoid overwriting values
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = row[j-1] + row[j]
            row = new_row
        return row