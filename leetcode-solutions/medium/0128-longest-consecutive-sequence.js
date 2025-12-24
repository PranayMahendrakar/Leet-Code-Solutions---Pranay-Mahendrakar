# Problem: Longest Consecutive Sequence
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Runtime: 34 ms
# Memory: 81.3 MB

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const set = new Set(nums);
    let maxLen = 0;
    
    for (const num of set) {
        // Only start counting if num is the start of a sequence
        if (!set.has(num - 1)) {
            let curr = num;
            let len = 1;
            
            while (set.has(curr + 1)) {
                curr++;
                len++;
            }
            
            maxLen = Math.max(maxLen, len);
        }
    }
    
    return maxLen;
};