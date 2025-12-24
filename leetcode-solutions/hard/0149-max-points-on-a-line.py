# Problem: Max Points on a Line
# Difficulty: Hard
# URL: https://leetcode.com/problems/max-points-on-a-line/
# Runtime: 29 ms
# Memory: 17.3 MB

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd
        from collections import defaultdict
        
        n = len(points)
        if n <= 2:
            return n
        
        result = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 0
            local_max = 0
            
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                # Normalize slope using GCD
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Make slope canonical (handle negative cases)
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                
                slope = (dx, dy)
                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])
            
            result = max(result, local_max + duplicate + 1)
        
        return result