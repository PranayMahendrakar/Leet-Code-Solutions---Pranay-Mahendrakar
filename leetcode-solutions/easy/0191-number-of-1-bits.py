# Problem: Number of 1 Bits
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-1-bits/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
        def hammingWeight(self, n):
                return bin(n).count('1')