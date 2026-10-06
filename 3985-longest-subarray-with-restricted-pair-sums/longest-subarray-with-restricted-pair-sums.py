class Solution(object):
    def maxSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = max(nums)
        cnt = [0] * (top + 1)

        def triples(x):
            # bad triples the window forms together with one extra element x
            t = 0
            for a in range(1, (x + 1) // 2):       # a + (x - a) == x, a < x - a
                t += cnt[a] * cnt[x - a]
            if x % 2 == 0:
                c = cnt[x // 2]
                t += c * (c - 1) // 2
            for a in range(1, top - x + 1):         # x + a == (x + a)
                t += cnt[a] * cnt[a + x]
            return t

        bad = 0
        left = 0
        best = 0
        for right, x in enumerate(nums):
            bad += triples(x)
            cnt[x] += 1
            while bad:
                y = nums[left]
                cnt[y] -= 1
                bad -= triples(y)
                left += 1
            if right - left + 1 > best:
                best = right - left + 1
        return best