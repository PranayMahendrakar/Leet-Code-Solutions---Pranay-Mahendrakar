# Problem: Combination Sum III
# Difficulty: Medium
# URL: https://leetcode.com/problems/combination-sum-iii/
# Runtime: 0 ms
# Memory: 54 MB

/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 * O(C(9,k)) time and space - Backtracking
 */
var combinationSum3 = function(k, n) {
    const result = [];
    
    const backtrack = (start, remaining, path) => {
        if (path.length === k && remaining === 0) {
            result.push([...path]);
            return;
        }
        if (path.length >= k || remaining <= 0) return;
        
        for (let i = start; i <= 9; i++) {
            if (i > remaining) break; // Pruning
            path.push(i);
            backtrack(i + 1, remaining - i, path);
            path.pop();
        }
    };
    
    backtrack(1, n, []);
    return result;
};