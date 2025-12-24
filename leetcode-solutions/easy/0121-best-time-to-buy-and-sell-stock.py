# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 91 ms
# Memory: 26.3 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit