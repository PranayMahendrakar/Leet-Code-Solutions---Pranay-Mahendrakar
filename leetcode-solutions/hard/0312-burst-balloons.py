# Problem: Burst Balloons
# Difficulty: Hard
# URL: https://leetcode.com/problems/burst-balloons/
# Runtime: 3297 ms
# Memory: 14.5 MB

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Add virtual balloons at boundaries
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] = max coins from bursting all balloons between i and j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # Iterate by gap size
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                # Try each balloon as the last one to burst in range (left, right)
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        return dp[0][n - 1]