class Solution(object):
    def maxEarnings(self, meetings):
        """
        :type meetings: List[List[int]]
        :rtype: int
        """
        n = len(meetings)
        by_end = sorted(range(n), key=lambda i: meetings[i][1])
        f = [0] * n      # best earnings of a schedule whose last meeting is i
        ptr = 0
        best_prev = None  # max of f[j] - end[j] over meetings already ended
        ans = 0
        for i in sorted(range(n), key=lambda i: meetings[i][0]):
            s, e, r = meetings[i]
            while ptr < n and meetings[by_end[ptr]][1] <= s:
                j = by_end[ptr]
                v = f[j] - meetings[j][1]
                if best_prev is None or v > best_prev:
                    best_prev = v
                ptr += 1
            f[i] = r if best_prev is None else r + s + best_prev
            if f[i] > ans:
                ans = f[i]
        return ans