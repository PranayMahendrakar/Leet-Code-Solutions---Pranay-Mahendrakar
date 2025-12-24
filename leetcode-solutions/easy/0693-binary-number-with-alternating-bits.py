# Problem: Binary Number with Alternating Bits
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-number-with-alternating-bits/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def hasAlternatingBits(self, n):
        prev = n & 1
        n >>= 1
        while n:
            curr = n & 1
            if curr == prev:
                return False
            prev = curr
            n >>= 1
        return True