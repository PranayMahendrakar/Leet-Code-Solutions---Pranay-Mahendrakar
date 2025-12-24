# Problem: Min Cost Climbing Stairs
# Difficulty: Easy
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/
# Runtime: 4 ms
# Memory: 12.5 MB

class Solution(object):
    def minCostClimbingStairs(self, cost):
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)