# Problem: Degree of an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/degree-of-an-array/
# Runtime: 19 ms
# Memory: 13.3 MB

class Solution(object):
    def findShortestSubArray(self, nums):
        first = {}
        last = {}
        count = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        result = len(nums)
        for num in count:
            if count[num] == degree:
                result = min(result, last[num] - first[num] + 1)
        return result