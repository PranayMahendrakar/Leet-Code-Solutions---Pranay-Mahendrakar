# Problem: Best Time to Buy and Sell Stock III
# Difficulty: Hard
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Runtime: 235 ms
# Memory: 20.8 MB

class Solution(object):
    def maxProfit(self, prices):
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        
        return sell2