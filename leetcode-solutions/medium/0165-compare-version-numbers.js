# Problem: Compare Version Numbers
# Difficulty: Medium
# URL: https://leetcode.com/problems/compare-version-numbers/
# Runtime: 0 ms
# Memory: 52.1 MB

/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 * O(n+m) time, O(n+m) space
 */
var compareVersion = function(version1, version2) {
    const v1 = version1.split('.');
    const v2 = version2.split('.');
    const maxLen = Math.max(v1.length, v2.length);
    
    for (let i = 0; i < maxLen; i++) {
        const num1 = i < v1.length ? parseInt(v1[i]) : 0;
        const num2 = i < v2.length ? parseInt(v2[i]) : 0;
        
        if (num1 < num2) return -1;
        if (num1 > num2) return 1;
    }
    
    return 0;
};