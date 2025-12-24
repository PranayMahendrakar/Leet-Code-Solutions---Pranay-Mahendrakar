# Problem: Best Position for a Service Centre
# Difficulty: Hard
# URL: https://leetcode.com/problems/best-position-for-a-service-centre/
# Runtime: 107 ms
# Memory: 17.4 MB

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        import math
        
        # Start from centroid
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        
        def total_dist(cx, cy):
            return sum(math.sqrt((cx - px)**2 + (cy - py)**2) for px, py in positions)
        
        # Gradient descent with decreasing step size
        step = 100.0
        
        while step > 1e-7:
            improved = False
            for dx, dy in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                nx, ny = x + dx, y + dy
                if total_dist(nx, ny) < total_dist(x, y):
                    x, y = nx, ny
                    improved = True
                    break
            
            if not improved:
                step /= 2
        
        return total_dist(x, y)