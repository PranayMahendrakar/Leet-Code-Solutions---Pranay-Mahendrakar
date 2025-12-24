# Problem: Number of Islands
# Difficulty: Medium
# URL: https://leetcode.com/problems/number-of-islands/
# Runtime: 58 ms
# Memory: 59 MB

/**
 * @param {character[][]} grid
 * @return {number}
 * O(m*n) time, O(m*n) space - DFS
 */
var numIslands = function(grid) {
    if (!grid || grid.length === 0) return 0;
    
    const m = grid.length, n = grid[0].length;
    let count = 0;
    
    const dfs = (i, j) => {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === '0') return;
        
        grid[i][j] = '0'; // Mark as visited
        dfs(i + 1, j);
        dfs(i - 1, j);
        dfs(i, j + 1);
        dfs(i, j - 1);
    };
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === '1') {
                count++;
                dfs(i, j);
            }
        }
    }
    
    return count;
};