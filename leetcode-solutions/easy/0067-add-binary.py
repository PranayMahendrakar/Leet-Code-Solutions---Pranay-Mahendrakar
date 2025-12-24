# Problem: Add Binary
# Difficulty: Easy
# URL: https://leetcode.com/problems/add-binary/
# Runtime: 1 ms
# Memory: 12.4 MB

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]