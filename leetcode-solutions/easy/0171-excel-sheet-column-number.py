# Problem: Excel Sheet Column Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/excel-sheet-column-number/
# Runtime: 0 ms
# Memory: 17.2 MB

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result