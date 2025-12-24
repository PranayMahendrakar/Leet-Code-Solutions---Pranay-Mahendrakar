# Problem: Remove Invalid Parentheses
# Difficulty: Hard
# URL: https://leetcode.com/problems/remove-invalid-parentheses/
# Runtime: 122 ms
# Memory: 12.9 MB

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for c in string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        # BFS to find minimum removals
        from collections import deque
        
        result = []
        visited = {s}
        queue = deque([s])
        found = False
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if is_valid(curr):
                    result.append(curr)
                    found = True
                
                if found:
                    continue  # Don't generate more after finding valid ones
                
                # Try removing each parenthesis
                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    
                    next_str = curr[:i] + curr[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
            
            if found:
                break
        
        return result if result else [""]