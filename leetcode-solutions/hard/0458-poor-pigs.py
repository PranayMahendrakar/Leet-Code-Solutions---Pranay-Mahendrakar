# Problem: Poor Pigs
# Difficulty: Hard
# URL: https://leetcode.com/problems/poor-pigs/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        import math
        # Each pig can test (minutesToTest // minutesToDie + 1) states
        states = minutesToTest // minutesToDie + 1
        
        # We need states^pigs >= buckets
        if buckets == 1:
            return 0
        
        pigs = 0
        while states ** pigs < buckets:
            pigs += 1
        return pigs