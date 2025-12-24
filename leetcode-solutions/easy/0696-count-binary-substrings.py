# Problem: Count Binary Substrings
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-binary-substrings/
# Runtime: 85 ms
# Memory: 14.5 MB

class Solution(object):
    def countBinarySubstrings(self, s):
        prev, curr, result = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1
        return result + min(prev, curr)