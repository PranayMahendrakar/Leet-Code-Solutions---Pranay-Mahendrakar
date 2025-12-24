# Problem: Difference Between Element Sum and Digit Sum of an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Runtime: 55 ms
# Memory: 12.8 MB

class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = sum(int(d) for num in nums for d in str(num))
        return abs(element_sum - digit_sum)