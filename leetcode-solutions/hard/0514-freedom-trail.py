# Problem: Freedom Trail
# Difficulty: Hard
# URL: https://leetcode.com/problems/freedom-trail/
# Runtime: 75 ms
# Memory: 18.3 MB

class Solution:
    def findRotateSteps(self, ring, key):
        from functools import lru_cache
        from collections import defaultdict
        
        n = len(ring)
        # Precompute positions of each character
        char_pos = defaultdict(list)
        for i, c in enumerate(ring):
            char_pos[c].append(i)
        
        @lru_cache(maxsize=None)
        def dp(ring_idx, key_idx):
            if key_idx == len(key):
                return 0
            
            min_steps = float('inf')
            for pos in char_pos[key[key_idx]]:
                # Calculate minimum rotation distance
                dist = abs(pos - ring_idx)
                dist = min(dist, n - dist)
                # Add 1 for pressing the button
                min_steps = min(min_steps, dist + 1 + dp(pos, key_idx + 1))
            
            return min_steps
        
        return dp(0, 0)