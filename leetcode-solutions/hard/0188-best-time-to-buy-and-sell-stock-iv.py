# Problem: Best Time to Buy and Sell Stock IV
# Difficulty: Hard
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Runtime: 51 ms
# Memory: 12.6 MB

class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        
        # If k >= n//2, unlimited transactions
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))
        
        # O(k) space DP
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j-1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        
        return sell[k]