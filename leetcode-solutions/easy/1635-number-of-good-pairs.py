# Problem: Number of Good Pairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-good-pairs/
# Runtime: 0 ms
# Memory: 17.3 MB

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        for num in nums:
            if num in count:
                result += count[num]
                count[num] += 1
            else:
                count[num] = 1
        return result