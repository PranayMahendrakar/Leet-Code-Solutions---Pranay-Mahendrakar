# Problem: Interleaving String
# Difficulty: Medium
# URL: https://leetcode.com/problems/interleaving-string/
# Runtime: 67 ms
# Memory: 56.1 MB

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    const m = s1.length, n = s2.length;
    if (m + n !== s3.length) return false;
    
    // O(n) space DP
    const dp = new Array(n + 1).fill(false);
    
    for (let i = 0; i <= m; i++) {
        for (let j = 0; j <= n; j++) {
            if (i === 0 && j === 0) {
                dp[j] = true;
            } else if (i === 0) {
                dp[j] = dp[j - 1] && s2[j - 1] === s3[j - 1];
            } else if (j === 0) {
                dp[j] = dp[j] && s1[i - 1] === s3[i - 1];
            } else {
                dp[j] = (dp[j] && s1[i - 1] === s3[i + j - 1]) ||
                        (dp[j - 1] && s2[j - 1] === s3[i + j - 1]);
            }
        }
    }
    
    return dp[n];
};