# Problem: 24 Game
# Difficulty: Hard
# URL: https://leetcode.com/problems/24-game/
# Runtime: 43 ms
# Memory: 12.6 MB

class Solution:
    def judgePoint24(self, cards):
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-9
            
            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    # Remaining numbers
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    # Try all operations
                    for op in ['+', '-', '*', '/']:
                        # Skip redundant cases
                        if op in ['+', '*'] and i > j:
                            continue
                        
                        a, b = nums[i], nums[j]
                        
                        if op == '+':
                            result = a + b
                        elif op == '-':
                            result = a - b
                        elif op == '*':
                            result = a * b
                        elif op == '/':
                            if abs(b) < 1e-9:
                                continue
                            result = a / b
                        
                        if solve(remaining + [result]):
                            return True
            
            return False
        
        return solve([float(c) for c in cards])