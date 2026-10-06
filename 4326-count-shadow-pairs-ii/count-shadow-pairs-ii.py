from bisect import bisect_right


class Solution(object):
    def shadowPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Rank the values. Among equal values the earlier index gets the larger
        # rank, so equal values never form a pair and never block one.
        pos = sorted(range(n), key=lambda i: (nums[i], -i))  # rank -> index
        p = [0] * n                                           # index -> rank
        for rank, i in enumerate(pos):
            p[i] = rank
        total = [0]

        def solve(l, r):
            # counts pairs inside [l, r) and returns its ranks in sorted order
            if r - l <= 32:
                c = 0
                for i in range(l, r):
                    a = p[i]
                    cur = n
                    for j in range(i + 1, r):
                        b = p[j]
                        if a < b < cur:
                            c += 1
                            cur = b
                total[0] += c
                return sorted(p[l:r])
            mid = (l + r) // 2
            merged = solve(l, mid) + solve(mid, r)
            merged.sort()
            c = 0
            left = []   # left-half ranks still unblocked: indices decreasing
            right = []  # right-half ranks: indices increasing
            for v in merged:
                x = pos[v]
                if x < mid:
                    while left and pos[left[-1]] < x:
                        left.pop()
                    left.append(v)
                else:
                    while right and pos[right[-1]] > x:
                        right.pop()
                    if right:
                        c += len(left) - bisect_right(left, right[-1])
                    else:
                        c += len(left)
                    right.append(v)
            total[0] += c
            return merged

        solve(0, n)
        return total[0]