from bisect import bisect_left


class Solution(object):
    _pals = None

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if Solution._pals is None:
            # all palindromes with up to 9 digits, in increasing order, split by parity
            even, odd = [], []
            for length in range(1, 10):
                half = (length + 1) // 2
                for h in range(10 ** (half - 1), 10 ** half):
                    s = str(h)
                    p = int(s + (s[-2::-1] if length % 2 else s[::-1]))
                    (odd if p % 2 else even).append(p)
            Solution._pals = (even, odd)

        ops = 0
        for x in nums:
            pals = Solution._pals[x % 2]  # +-2 never changes parity
            i = bisect_left(pals, x)
            best = float('inf')
            if i < len(pals):
                best = pals[i] - x
            if i > 0:
                best = min(best, x - pals[i - 1])
            ops += best // 2
        return ops