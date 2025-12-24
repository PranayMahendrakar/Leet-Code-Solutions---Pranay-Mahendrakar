# Problem: Count the Digits That Divide a Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Runtime: 0 ms
# Memory: 12.3 MB

class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num
        while n > 0:
            digit = n % 10
            if num % digit == 0:
                count += 1
            n //= 10
        return count