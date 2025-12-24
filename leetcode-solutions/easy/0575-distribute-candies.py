# Problem: Distribute Candies
# Difficulty: Easy
# URL: https://leetcode.com/problems/distribute-candies/
# Runtime: 23 ms
# Memory: 14.3 MB

class Solution(object):
    def distributeCandies(self, candyType):
        return min(len(set(candyType)), len(candyType) // 2)