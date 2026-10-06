class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG = float('-inf')
        # A = alternating prefix sum; for a rotation of nums[l..r] the gain is
        #   2 * (A[l+1] - A[r+1]) if l and r have the same parity
        #   2 * (A[l]   - A[r+1]) otherwise
        same = [NEG, NEG]  # max A[l+1] over earlier l, by parity of l
        diff = [NEG, NEG]  # max A[l]   over earlier l, by parity of l
        prefix = 0         # A[r]
        best = 0
        for r, x in enumerate(nums):
            par = r & 1
            nxt = prefix - x if par else prefix + x  # A[r+1]
            gain = max(same[par], diff[1 - par]) - nxt
            if gain > best:
                best = gain
            if nxt > same[par]:
                same[par] = nxt
            if prefix > diff[par]:
                diff[par] = prefix
            prefix = nxt
        return prefix + 2 * best