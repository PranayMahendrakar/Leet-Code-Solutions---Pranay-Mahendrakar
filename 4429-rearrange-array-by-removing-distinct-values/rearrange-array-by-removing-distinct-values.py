from collections import Counter

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = Counter(nums)
        values = sorted(counts)
        ans = []

        while values:
            remaining = []

            for value in values:
                ans.append(value)
                counts[value] -= 1

                if counts[value] > 0:
                    remaining.append(value)

            values = remaining

        return ans