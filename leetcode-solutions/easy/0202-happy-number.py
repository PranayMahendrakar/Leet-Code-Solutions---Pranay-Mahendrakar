# Problem: Happy Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/happy-number/
# Runtime: 6 ms
# Memory: 12.4 MB

class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1