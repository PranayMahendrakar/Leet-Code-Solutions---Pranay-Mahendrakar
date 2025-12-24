# Problem: Maximum Gap
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-gap/
# Runtime: 38 ms
# Memory: 82.4 MB

/**
 * @param {number[]} nums
 * @return {number}
 * O(n) time, O(n) space - Bucket Sort / Pigeonhole Principle
 */
var maximumGap = function(nums) {
    const n = nums.length;
    if (n < 2) return 0;
    
    let min = Math.min(...nums);
    let max = Math.max(...nums);
    
    if (min === max) return 0;
    
    // Bucket size and count
    const bucketSize = Math.max(1, Math.floor((max - min) / (n - 1)));
    const bucketCount = Math.floor((max - min) / bucketSize) + 1;
    
    // Initialize buckets with min/max for each
    const bucketsMin = new Array(bucketCount).fill(Infinity);
    const bucketsMax = new Array(bucketCount).fill(-Infinity);
    
    // Place each number in its bucket
    for (const num of nums) {
        const idx = Math.floor((num - min) / bucketSize);
        bucketsMin[idx] = Math.min(bucketsMin[idx], num);
        bucketsMax[idx] = Math.max(bucketsMax[idx], num);
    }
    
    // Maximum gap is between consecutive non-empty buckets
    let maxGap = 0;
    let prevMax = bucketsMax[0];
    
    for (let i = 1; i < bucketCount; i++) {
        if (bucketsMin[i] === Infinity) continue; // Empty bucket
        maxGap = Math.max(maxGap, bucketsMin[i] - prevMax);
        prevMax = bucketsMax[i];
    }
    
    return maxGap;
};