# Problem: Find Peak Element
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-peak-element/
# Runtime: 0 ms
# Memory: 54.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 * O(log n) time, O(1) space - Binary Search
 */
var findPeakElement = function(nums) {
    let left = 0, right = nums.length - 1;
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        
        // If mid is on ascending slope, peak is on the right
        if (nums[mid] < nums[mid + 1]) {
            left = mid + 1;
        } else {
            // If mid is on descending slope, peak is on the left (including mid)
            right = mid;
        }
    }
    
    // When left === right, we've found a peak
    return left;
};