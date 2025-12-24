# Problem: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Runtime: 2 ms
# Memory: 55.4 MB

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 * O(n) time, O(1) space - Two pointers
 */
var twoSum = function(numbers, target) {
    let left = 0, right = numbers.length - 1;
    
    while (left < right) {
        const sum = numbers[left] + numbers[right];
        
        if (sum === target) {
            return [left + 1, right + 1]; // 1-indexed
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return [-1, -1]; // Should never reach here
};