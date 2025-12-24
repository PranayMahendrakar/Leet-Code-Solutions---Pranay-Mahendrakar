# Problem: Nim Game
# Difficulty: Easy
# URL: https://leetcode.com/problems/nim-game/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0