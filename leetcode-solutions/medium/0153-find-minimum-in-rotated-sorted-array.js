# Problem: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Runtime: 0 ms
# Memory: 53.9 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0, right = nums.length - 1;
    
    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return nums[left];
};