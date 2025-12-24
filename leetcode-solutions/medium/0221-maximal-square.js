# Problem: Maximal Square
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximal-square/
# Runtime: 15 ms
# Memory: 61.8 MB

/**
 * @param {character[][]} matrix
 * @return {number}
 * O(m*n) time, O(n) space - Space optimized DP
 */
var maximalSquare = function(matrix) {
    if (!matrix || matrix.length === 0) return 0;
    
    const m = matrix.length, n = matrix[0].length;
    let prev = new Array(n + 1).fill(0);
    let curr = new Array(n + 1).fill(0);
    let maxSide = 0;
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (matrix[i-1][j-1] === '1') {
                curr[j] = Math.min(prev[j-1], prev[j], curr[j-1]) + 1;
                maxSide = Math.max(maxSide, curr[j]);
            } else {
                curr[j] = 0;
            }
        }
        [prev, curr] = [curr, prev];
        curr.fill(0);
    }
    
    return maxSide * maxSide;
};