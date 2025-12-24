# Problem: Kth Smallest Number in Multiplication Table
# Difficulty: Hard
# URL: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# Runtime: 547 ms
# Memory: 13.2 MB

class Solution:
    def findKthNumber(self, m, n, k):
        def count_less_equal(x):
            # Count how many numbers in the table are <= x
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count
        
        left, right = 1, m * n
        
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        return left