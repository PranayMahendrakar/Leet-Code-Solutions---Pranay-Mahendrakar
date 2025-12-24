# Problem: Dungeon Game
# Difficulty: Hard
# URL: https://leetcode.com/problems/dungeon-game/
# Runtime: 6 ms
# Memory: 13.1 MB

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        
        # O(n) space - use single row
        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        
        return dp[0]