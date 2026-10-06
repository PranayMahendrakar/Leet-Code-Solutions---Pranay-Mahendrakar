class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        doubled = [(2 * x) % k for x in nums]
        best = 0
        for l in range(n):
            if n - l <= best:
                break  # nothing longer can start here
            total = 0
            seen = set()  # values of 2*x mod k inside nums[l..r]
            for r in range(l, n):
                total = (total + nums[r]) % k
                seen.add(doubled[r])
                # negating x changes the sum by -2x, so we need 2x == sum (mod k)
                if (total == 0 or total in seen) and r - l + 1 > best:
                    best = r - l + 1
        return best