class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_needed = 0   # unmatched ')' needing a '('
        close_needed = 0  # unmatched '(' needing a ')'
        for c in s:
            if c == '(':
                close_needed += 1
            elif close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1
        return open_needed + close_needed