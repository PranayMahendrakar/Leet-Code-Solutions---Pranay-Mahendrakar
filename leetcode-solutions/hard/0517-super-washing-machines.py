# Problem: Super Washing Machines
# Difficulty: Hard
# URL: https://leetcode.com/problems/super-washing-machines/
# Runtime: 8 ms
# Memory: 13.2 MB

class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        
        if total % n != 0:
            return -1
        
        target = total // n
        result = 0
        balance = 0  # Running balance from left
        
        for dresses in machines:
            balance += dresses - target
            # Max of: abs(running balance), excess in current machine
            result = max(result, abs(balance), dresses - target)
        
        return result