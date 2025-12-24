# Problem: Shortest Subarray with Sum at Least K
# Difficulty: Hard
# URL: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Runtime: 288 ms
# Memory: 23.9 MB

class Solution:
    def shortestSubarray(self, nums, k):
        from collections import deque
        
        n = len(nums)
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        result = n + 1
        dq = deque()  # Store indices
        
        for i in range(n + 1):
            # Check if current prefix - some earlier prefix >= k
            while dq and prefix[i] - prefix[dq[0]] >= k:
                result = min(result, i - dq.popleft())
            
            # Maintain increasing monotonic queue
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return result if result <= n else -1