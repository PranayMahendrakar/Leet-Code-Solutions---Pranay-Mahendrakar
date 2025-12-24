# Problem: Bitwise AND of Numbers Range
# Difficulty: Medium
# URL: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Runtime: 5 ms
# Memory: 62.6 MB

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 * O(log n) time, O(1) space - Find common prefix
 */
var rangeBitwiseAnd = function(left, right) {
    let shift = 0;
    
    // Find common prefix by right shifting until left == right
    while (left < right) {
        left >>= 1;
        right >>= 1;
        shift++;
    }
    
    // Shift back to restore the common prefix
    return left << shift;
};