# Problem: Subsets II
# Difficulty: Medium
# URL: https://leetcode.com/problems/subsets-ii/
# Runtime: 0 ms
# Memory: 12.8 MB

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()
        
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result