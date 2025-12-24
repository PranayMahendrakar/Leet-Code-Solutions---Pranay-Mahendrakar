# Problem: Making A Large Island
# Difficulty: Hard
# URL: https://leetcode.com/problems/making-a-large-island/
# Runtime: 1528 ms
# Memory: 21.2 MB

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        
        def dfs(i, j, island_id):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id
            return 1 + dfs(i+1, j, island_id) + dfs(i-1, j, island_id) + dfs(i, j+1, island_id) + dfs(i, j-1, island_id)
        
        # Label islands and compute sizes
        island_sizes = {0: 0}
        island_id = 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1
        
        # Try flipping each 0
        result = max(island_sizes.values()) if island_sizes else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            neighbors.add(grid[ni][nj])
                    
                    new_size = 1 + sum(island_sizes.get(iid, 0) for iid in neighbors)
                    result = max(result, new_size)
        
        return result