# Problem: Majority Element
# Difficulty: Easy
# URL: https://leetcode.com/problems/majority-element/
# Runtime: 9 ms
# Memory: 13.7 MB

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate