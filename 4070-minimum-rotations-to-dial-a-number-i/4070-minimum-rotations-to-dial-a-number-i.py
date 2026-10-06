class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        total = 0
        for ch in s:
            d = int(ch)
            diff = abs(d - cur)
            total += min(diff, 10 - diff)
            cur = d
        return total