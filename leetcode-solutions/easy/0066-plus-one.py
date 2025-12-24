# Problem: Plus One
# Difficulty: Easy
# URL: https://leetcode.com/problems/plus-one/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # All digits were 9, need to add 1 at the beginning
        return [1] + digits