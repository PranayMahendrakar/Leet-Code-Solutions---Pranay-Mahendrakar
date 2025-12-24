# Problem: Number of Digit One
# Difficulty: Hard
# URL: https://leetcode.com/problems/number-of-digit-one/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        count = 0
        factor = 1
        
        while factor <= n:
            # Divide number into: higher, current, lower
            lower = n % factor
            current = (n // factor) % 10
            higher = n // (factor * 10)
            
            if current == 0:
                # Only higher digits contribute
                count += higher * factor
            elif current == 1:
                # Higher digits + partial from current
                count += higher * factor + lower + 1
            else:
                # Current digit >= 2, all combinations possible
                count += (higher + 1) * factor
            
            factor *= 10
        
        return count