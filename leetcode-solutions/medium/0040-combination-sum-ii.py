# Problem: Combination Sum II
# Difficulty: Medium
# URL: https://leetcode.com/problems/combination-sum-ii/
# Runtime: 36 ms
# Memory: 12.6 MB

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return result