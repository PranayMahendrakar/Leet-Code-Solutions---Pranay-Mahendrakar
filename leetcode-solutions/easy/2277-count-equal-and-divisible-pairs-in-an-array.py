# Problem: Count Equal and Divisible Pairs in an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# Runtime: 35 ms
# Memory: 12.3 MB

class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count