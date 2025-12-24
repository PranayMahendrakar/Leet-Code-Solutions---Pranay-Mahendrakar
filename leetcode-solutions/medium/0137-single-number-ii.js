# Problem: Single Number II
# Difficulty: Medium
# URL: https://leetcode.com/problems/single-number-ii/
# Runtime: 3 ms
# Memory: 56 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ones = 0, twos = 0;
    
    for (const num of nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }
    
    return ones;
};