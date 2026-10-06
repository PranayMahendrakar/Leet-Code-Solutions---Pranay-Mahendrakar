class Solution(object):
    def countRotations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # equal adjacent pairs treating s as a circle
        total = sum(1 for i in range(n) if s[i] == s[(i + 1) % n])
        # rotating by r only breaks the circular pair (s[r-1], s[r])
        return sum(1 for r in range(n) if total - (s[r - 1] == s[r]) == k)