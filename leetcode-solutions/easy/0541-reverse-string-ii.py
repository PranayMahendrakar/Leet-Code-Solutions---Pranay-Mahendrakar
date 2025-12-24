# Problem: Reverse String II
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-string-ii/
# Runtime: 3 ms
# Memory: 12.8 MB

class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)