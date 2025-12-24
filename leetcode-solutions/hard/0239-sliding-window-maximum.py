# Problem: Sliding Window Maximum
# Difficulty: Hard
# URL: https://leetcode.com/problems/sliding-window-maximum/
# Runtime: 308 ms
# Memory: 27.9 MB

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        
        dq = deque()  # stores indices
        result = []
        
        for i, num in enumerate(nums):
            # Remove elements outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove smaller elements
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result