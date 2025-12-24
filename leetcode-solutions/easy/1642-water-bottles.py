# Problem: Water Bottles
# Difficulty: Easy
# URL: https://leetcode.com/problems/water-bottles/
# Runtime: 0 ms
# Memory: 17.6 MB

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles
        
        return total