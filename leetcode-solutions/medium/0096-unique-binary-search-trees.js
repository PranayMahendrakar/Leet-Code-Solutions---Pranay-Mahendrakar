# Problem: Unique Binary Search Trees
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-binary-search-trees/
# Runtime: 0 ms
# Memory: 54.1 MB

/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    // Catalan number using DP: O(n^2) time, O(n) space
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    
    for (let i = 2; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            dp[i] += dp[j] * dp[i - 1 - j];
        }
    }
    
    return dp[n];
};