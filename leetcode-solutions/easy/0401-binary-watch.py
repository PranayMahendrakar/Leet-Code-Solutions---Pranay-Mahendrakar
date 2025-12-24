# Problem: Binary Watch
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-watch/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == turnedOn]