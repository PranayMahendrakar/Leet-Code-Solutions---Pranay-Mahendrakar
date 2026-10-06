class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        W = n + 2  # padded width; border cells hold -1 so every ray stops there
        INF = float('inf')
        g = [0] * ((m + 2) * W)
        F = [-1] * ((m + 2) * W)  # F[c] = min cost to reach c with the segments used so far
        for i in range(m):
            base = (i + 1) * W + 1
            g[base:base + n] = grid[i]
            F[base:base + n] = [INF] * n
        start, target = W + 1, m * W + n
        F[start] = g[start]
        N = F[:]  # values for the next layer
        changed = [start]
        dirs = (1, -1, W, -W)
        segments = 0
        while changed and segments <= k:  # k turns = k + 1 straight segments
            segments += 1
            touched = []
            for c0 in changed:
                v = F[c0]
                for d in dirs:
                    c = c0 + d
                    r = v + g[c]
                    while r < F[c]:
                        if r < N[c]:
                            N[c] = r
                            touched.append(c)
                        c += d
                        r += g[c]
            changed = set(touched)
            for c in changed:
                F[c] = N[c]
        return F[target] if F[target] != INF else -1