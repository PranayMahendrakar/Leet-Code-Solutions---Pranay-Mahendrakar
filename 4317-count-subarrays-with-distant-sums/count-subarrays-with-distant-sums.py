from bisect import bisect_left, bisect_right


class Solution(object):
    def distantSubarrays(self, nums, goal, k):
        """
        :type nums: List[int]
        :type goal: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        vals = sorted(set(prefix))
        m = len(vals)
        tree = [0] * (m + 1)
        close = 0  # subarrays with |sum - goal| < k
        for p in prefix:
            # earlier prefixes q with p - goal - k < q < p - goal + k
            lo = bisect_right(vals, p - goal - k)
            hi = bisect_left(vals, p - goal + k)
            if hi > lo:
                i = hi
                while i > 0:
                    close += tree[i]
                    i -= i & -i
                i = lo
                while i > 0:
                    close -= tree[i]
                    i -= i & -i
            i = bisect_left(vals, p) + 1
            while i <= m:
                tree[i] += 1
                i += i & -i
        return n * (n + 1) // 2 - close