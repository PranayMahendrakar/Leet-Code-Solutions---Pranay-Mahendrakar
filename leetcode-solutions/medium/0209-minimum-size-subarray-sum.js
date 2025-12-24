# Problem: Minimum Size Subarray Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/
# Runtime: 3 ms
# Memory: 58.8 MB

/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 * O(n) time, O(1) space - Sliding Window
 */
var minSubArrayLen = function(target, nums) {
    let left = 0, sum = 0;
    let minLen = Infinity;
    
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        
        while (sum >= target) {
            minLen = Math.min(minLen, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }
    
    return minLen === Infinity ? 0 : minLen;
};