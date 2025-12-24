# Problem: Number of Atoms
# Difficulty: Hard
# URL: https://leetcode.com/problems/number-of-atoms/
# Runtime: 4 ms
# Memory: 17.6 MB

class Solution:
    def countOfAtoms(self, formula):
        from collections import defaultdict
        
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                # Parse multiplier
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or 1)
                
                # Pop and merge
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * mult
            else:
                # Parse element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                
                # Parse count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                
                stack[-1][elem] += count
        
        # Build result
        result = stack[0]
        return ''.join(f"{elem}{result[elem] if result[elem] > 1 else ''}" 
                       for elem in sorted(result.keys()))