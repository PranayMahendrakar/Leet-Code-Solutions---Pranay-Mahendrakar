# Problem: House Robber
# Difficulty: Medium
# URL: https://leetcode.com/problems/house-robber/
# Runtime: 1 ms
# Memory: 53.1 MB

/**
 * @param {number[]} nums
 * @return {number}
 * O(n) time, O(1) space - Space optimized DP
 */
var rob = function(nums) {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];
    
    let prev2 = 0; // dp[i-2]
    let prev1 = 0; // dp[i-1]
    
    for (const num of nums) {
        const curr = Math.max(prev1, prev2 + num);
        prev2 = prev1;
        prev1 = curr;
    }
    
    return prev1;
};