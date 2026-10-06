class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positions = {}
        for i, x in enumerate(nums):
            positions.setdefault(x, []).append(i)
        count = 0
        for idx in positions.values():
            if len(idx) == 3 and idx[1] - idx[0] == idx[2] - idx[1]:
                count += 1
        return count