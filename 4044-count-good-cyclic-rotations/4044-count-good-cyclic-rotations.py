class Solution(object):
    def countGoodRotations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        half = n // 2
        total = sum(nums)
        window = sum(nums[:half])  # first half of rotation r
        count = 0
        for r in range(n):
            if 2 * window > total:
                count += 1
            # slide the circular window one step
            window += nums[(r + half) % n] - nums[r]
        return count