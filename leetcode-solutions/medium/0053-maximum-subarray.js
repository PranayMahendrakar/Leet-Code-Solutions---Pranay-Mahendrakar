# Problem: Maximum Subarray
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-subarray/
# Runtime: 3 ms
# Memory: 63.6 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = nums[0];
    let currentSum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i]);
        maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
};