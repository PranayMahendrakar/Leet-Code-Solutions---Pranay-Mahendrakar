# Problem: Number Complement
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-complement/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def findComplement(self, num):
        mask = (1 << num.bit_length()) - 1
        return num ^ mask