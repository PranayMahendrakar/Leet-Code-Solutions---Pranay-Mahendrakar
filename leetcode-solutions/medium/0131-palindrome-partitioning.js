# Problem: Palindrome Partitioning
# Difficulty: Medium
# URL: https://leetcode.com/problems/palindrome-partitioning/
# Runtime: 13 ms
# Memory: 79.5 MB

/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const result = [];
    const n = s.length;
    
    // Precompute palindrome table
    const dp = Array(n).fill(null).map(() => Array(n).fill(false));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i; j < n; j++) {
            if (s[i] === s[j] && (j - i <= 2 || dp[i + 1][j - 1])) {
                dp[i][j] = true;
            }
        }
    }
    
    const backtrack = (start, path) => {
        if (start === n) {
            result.push([...path]);
            return;
        }
        
        for (let end = start; end < n; end++) {
            if (dp[start][end]) {
                path.push(s.substring(start, end + 1));
                backtrack(end + 1, path);
                path.pop();
            }
        }
    };
    
    backtrack(0, []);
    return result;
};