# Problem: Valid Number
# Difficulty: Hard
# URL: https://leetcode.com/problems/valid-number/
# Runtime: 0 ms
# Memory: 12.4 MB

class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in '+-':
                if i > 0 and s[i-1].lower() != 'e':
                    return False
            elif c == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif c.lower() == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False  # Need digit after e
            else:
                return False
        
        return seen_digit