# Problem: Scramble String
# Difficulty: Hard
# URL: https://leetcode.com/problems/scramble-string/
# Runtime: 11 ms
# Memory: 17.8 MB

class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}
        
        def solve(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            if s1 == s2:
                return True
            
            if sorted(s1) != sorted(s2):
                return False
            
            n = len(s1)
            for i in range(1, n):
                # No swap
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Swap
                if solve(s1[:i], s2[n-i:]) and solve(s1[i:], s2[:n-i]):
                    memo[(s1, s2)] = True
                    return True
            
            memo[(s1, s2)] = False
            return False
        
        return solve(s1, s2)