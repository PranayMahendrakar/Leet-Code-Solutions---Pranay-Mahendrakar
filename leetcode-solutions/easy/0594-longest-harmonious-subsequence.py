# Problem: Longest Harmonious Subsequence
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-harmonious-subsequence/
# Runtime: 48 ms
# Memory: 14.6 MB

class Solution(object):
    def findLHS(self, nums):
        from collections import Counter
        count = Counter(nums)
        result = 0
        for num in count:
            if num + 1 in count:
                result = max(result, count[num] + count[num + 1])
        return result