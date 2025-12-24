# Problem: Largest Number
# Difficulty: Medium
# URL: https://leetcode.com/problems/largest-number/
# Runtime: 7 ms
# Memory: 58.3 MB

/**
 * @param {number[]} nums
 * @return {string}
 * O(n log n) time, O(n) space - Custom sort comparator
 */
var largestNumber = function(nums) {
    // Convert to strings and sort with custom comparator
    const strs = nums.map(String);
    
    strs.sort((a, b) => (b + a).localeCompare(a + b));
    
    // Handle edge case: all zeros
    if (strs[0] === '0') return '0';
    
    return strs.join('');
};