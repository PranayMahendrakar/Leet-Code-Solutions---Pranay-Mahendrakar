# Problem: Reverse Bits
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-bits/
# Runtime: 22 ms
# Memory: 12.3 MB

class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result