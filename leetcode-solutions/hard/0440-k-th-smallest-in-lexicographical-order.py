# Problem: K-th Smallest in Lexicographical Order
# Difficulty: Hard
# URL: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Runtime: 1 ms
# Memory: 12.6 MB

class Solution:
    def findKthNumber(self, n, k):
        def count_steps(n, curr, next_prefix):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return steps
        
        curr = 1
        k -= 1  # Start from 1, so we need k-1 more steps
        
        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                # Skip this subtree
                k -= steps
                curr += 1
            else:
                # Go deeper into this subtree
                k -= 1
                curr *= 10
        
        return curr