# Problem: Can Place Flowers
# Difficulty: Easy
# URL: https://leetcode.com/problems/can-place-flowers/
# Runtime: 12 ms
# Memory: 13.2 MB

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
        return count >= n