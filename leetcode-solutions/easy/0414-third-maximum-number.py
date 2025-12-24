# Problem: Third Maximum Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/third-maximum-number/
# Runtime: 0 ms
# Memory: 13.1 MB

class Solution(object):
    def thirdMax(self, nums):
        unique = list(set(nums))
        if len(unique) < 3:
            return max(unique)
        unique.sort(reverse=True)
        return unique[2]