class Solution(object):
    def maxEqualAdjacentPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        equal = 0
        best_gain = 0
        counts = {}

        for i in range(1, len(nums)):
            a, b = nums[i - 1], nums[i]

            if a == b:
                equal += 1
            else:
                if a > b:
                    a, b = b, a

                pair = (a, b)
                counts[pair] = counts.get(pair, 0) + 1
                best_gain = max(best_gain, counts[pair])

        return equal + best_gain