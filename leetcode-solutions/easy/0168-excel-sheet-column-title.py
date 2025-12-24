# Problem: Excel Sheet Column Title
# Difficulty: Easy
# URL: https://leetcode.com/problems/excel-sheet-column-title/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result