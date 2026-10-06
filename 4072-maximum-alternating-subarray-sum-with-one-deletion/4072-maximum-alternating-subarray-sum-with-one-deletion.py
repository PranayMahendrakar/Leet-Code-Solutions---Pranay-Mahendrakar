class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG = -10 ** 18
        # p = last element added, m = last element subtracted;
        # 0/1 = whether an element inside the subarray was deleted
        p0 = m0 = p1 = m1 = NEG
        p0_old = m0_old = NEG   # p0, m0 one position further back
        ans = NEG
        for x in nums:
            np0 = max(x, m0 + x)
            nm0 = p0 - x
            np1 = max(m1, m0_old) + x   # m0_old: the previous element is deleted
            nm1 = max(p1, p0_old) - x
            p0_old, m0_old = p0, m0
            p0, m0, p1, m1 = np0, nm0, np1, nm1
            ans = max(ans, p0, m0, p1, m1)
        return ans