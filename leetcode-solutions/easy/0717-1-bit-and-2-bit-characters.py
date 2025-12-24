# Problem: 1-bit and 2-bit Characters
# Difficulty: Easy
# URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1