# Problem: Max Consecutive Ones
# Difficulty: Easy
# URL: https://leetcode.com/problems/max-consecutive-ones/
# Runtime: 20 ms
# Memory: 13.5 MB

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count