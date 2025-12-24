# Problem: Fizz Buzz
# Difficulty: Easy
# URL: https://leetcode.com/problems/fizz-buzz/
# Runtime: 2 ms
# Memory: 13.4 MB

class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result