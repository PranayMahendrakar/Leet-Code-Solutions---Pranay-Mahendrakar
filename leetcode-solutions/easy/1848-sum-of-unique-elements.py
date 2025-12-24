# Problem: Sum of Unique Elements
# Difficulty: Easy
# URL: https://leetcode.com/problems/sum-of-unique-elements/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def sumOfUnique(self, nums):
        from collections import Counter
        count = Counter(nums)
        return sum(num for num, cnt in count.items() if cnt == 1)