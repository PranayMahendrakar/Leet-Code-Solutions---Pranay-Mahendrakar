# Problem: Richest Customer Wealth
# Difficulty: Easy
# URL: https://leetcode.com/problems/richest-customer-wealth/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(account) for account in accounts)