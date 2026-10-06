class Solution(object):
    _reach = None

    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if Solution._reach is None:
            N = 100000
            tri = []
            a = 1
            while a * (a + 1) // 2 <= N:
                tri.append(a * (a + 1) // 2)
                a += 1
            mask = (1 << (N + 1)) - 1
            # reach[c]: bit v is set if score v is reachable with
            # (total streak days + number of streaks) == c
            reach = [1]
            seen = 1
            c = 0
            while seen != mask:
                c += 1
                cur = 0
                for a in range(1, min(c - 1, len(tri)) + 1):
                    cur |= reach[c - a - 1] << tri[a - 1]
                cur &= mask
                reach.append(cur)
                seen |= cur
            Solution._reach = reach
        reach = Solution._reach
        c = 0
        while not (reach[c] >> n) & 1:
            c += 1
        return c - 1  # the last streak needs no skip after it