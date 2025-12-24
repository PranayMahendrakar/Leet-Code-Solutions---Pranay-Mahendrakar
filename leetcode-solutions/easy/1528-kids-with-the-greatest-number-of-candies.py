# Problem: Kids With the Greatest Number of Candies
# Difficulty: Easy
# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Runtime: 0 ms
# Memory: 12.6 MB

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]