# Problem: Maximum Product Subarray
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-product-subarray/
# Runtime: 2 ms
# Memory: 56.1 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let maxProd = nums[0];
    let minSoFar = nums[0];
    let maxSoFar = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        const num = nums[i];
        const tempMax = Math.max(num, maxSoFar * num, minSoFar * num);
        minSoFar = Math.min(num, maxSoFar * num, minSoFar * num);
        maxSoFar = tempMax;
        maxProd = Math.max(maxProd, maxSoFar);
    }
    
    return maxProd;
};