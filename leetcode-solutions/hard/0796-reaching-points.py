# Problem: Reaching Points
# Difficulty: Hard
# URL: https://leetcode.com/problems/reaching-points/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        # Work backwards from target to source
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                if ty == sy:
                    # Check if we can reach sx from tx by subtracting ty
                    return (tx - sx) % ty == 0
                tx %= ty
            else:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx
        
        return False