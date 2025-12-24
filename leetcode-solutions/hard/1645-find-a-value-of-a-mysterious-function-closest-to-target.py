# Problem: Find a Value of a Mysterious Function Closest to Target
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
# Runtime: 514 ms
# Memory: 26.7 MB

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        result = float('inf')
        current = set()
        
        for num in arr:
            # Each element ANDed with all previous cumulative ANDs
            current = {num & prev for prev in current} | {num}
            
            # Check each value against target
            for val in current:
                result = min(result, abs(val - target))
        
        return result