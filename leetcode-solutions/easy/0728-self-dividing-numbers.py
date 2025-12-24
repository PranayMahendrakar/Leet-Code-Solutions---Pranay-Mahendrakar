# Problem: Self Dividing Numbers
# Difficulty: Easy
# URL: https://leetcode.com/problems/self-dividing-numbers/
# Runtime: 7 ms
# Memory: 12.8 MB

class Solution(object):
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(n):
            original = n
            while n:
                digit = n % 10
                if digit == 0 or original % digit != 0:
                    return False
                n //= 10
            return True
        return [n for n in range(left, right + 1) if is_self_dividing(n)]