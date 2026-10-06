class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # x -> [last index, gap, occurrence count, still equally spaced]
        info = {}
        for i, x in enumerate(nums):
            if x not in info:
                info[x] = [i, 0, 1, True]
                continue
            e = info[x]
            gap = i - e[0]
            if e[2] == 1:
                e[1] = gap
            elif gap != e[1]:
                e[3] = False
            e[0] = i
            e[2] += 1
        return sum(1 for e in info.values() if e[2] >= 3 and e[3])