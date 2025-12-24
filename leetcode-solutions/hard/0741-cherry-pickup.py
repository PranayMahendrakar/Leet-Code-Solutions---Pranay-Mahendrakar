# Problem: Cherry Pickup
# Difficulty: Hard
# URL: https://leetcode.com/problems/cherry-pickup/
# Runtime: 556 ms
# Memory: 57.5 MB

class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}
        
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            
            # Cherries collected at current positions
            cherries = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]
            
            # Try all 4 combinations of moves
            best = max(
                dp(r1 + 1, c1, r2 + 1),  # both down
                dp(r1 + 1, c1, r2),      # first down, second right
                dp(r1, c1 + 1, r2 + 1),  # first right, second down
                dp(r1, c1 + 1, r2)       # both right
            )
            
            result = cherries + best
            memo[(r1, c1, r2)] = result
            return result
        
        result = dp(0, 0, 0)
        return max(0, result)