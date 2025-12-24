# Problem: Sliding Window Median
# Difficulty: Hard
# URL: https://leetcode.com/problems/sliding-window-median/
# Runtime: 266 ms
# Memory: 28.5 MB

class Solution:
    def medianSlidingWindow(self, nums, k):
        from sortedcontainers import SortedList
        
        window = SortedList()
        result = []
        
        for i, num in enumerate(nums):
            window.add(num)
            
            # Remove element going out of window
            if i >= k:
                window.remove(nums[i - k])
            
            # Calculate median when window is full
            if i >= k - 1:
                if k % 2 == 1:
                    result.append(float(window[k // 2]))
                else:
                    result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        
        return result