class Solution(object):
    def minRotations(self, n, s):
        """
        :type n: int
        :type s: str
        :rtype: int
        """
        def dist(a, b):
            diff = abs(a - b)
            return min(diff, 10 - diff)

        digits = [int(ch) for ch in s]
        last = digits[-1]
        total = 0
        best_change = 0  # no reversal
        prev = 0
        for d in digits:
            step = dist(prev, d)
            total += step
            # reversing the suffix that starts here only changes this one step:
            # the pointer now goes from prev to the old last digit instead
            change = dist(prev, last) - step
            if change < best_change:
                best_change = change
            prev = d
        return total + best_change