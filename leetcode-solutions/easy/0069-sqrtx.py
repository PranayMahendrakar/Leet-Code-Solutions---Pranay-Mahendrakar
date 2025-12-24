# Problem: Sqrt(x)
# Difficulty: Easy
# URL: https://leetcode.com/problems/sqrtx/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right