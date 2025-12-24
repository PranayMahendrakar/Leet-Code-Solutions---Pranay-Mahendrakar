# Problem: House Robber II
# Difficulty: Medium
# URL: https://leetcode.com/problems/house-robber-ii/
# Runtime: 0 ms
# Memory: 53.5 MB

/**
 * @param {number[]} nums
 * @return {number}
 * O(n) time, O(1) space - Two cases: exclude first or last house
 */
var rob = function(nums) {
    if (nums.length === 1) return nums[0];
    
    const robRange = (start, end) => {
        let prev2 = 0, prev1 = 0;
        for (let i = start; i <= end; i++) {
            const curr = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    };
    
    // Max of: rob houses 0 to n-2, or houses 1 to n-1
    return Math.max(
        robRange(0, nums.length - 2),
        robRange(1, nums.length - 1)
    );
};