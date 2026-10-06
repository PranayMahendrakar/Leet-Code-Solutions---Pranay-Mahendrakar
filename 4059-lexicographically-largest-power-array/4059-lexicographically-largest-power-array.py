class Solution(object):
    def largestPower(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Ordered blocks: elements may be freely reordered inside a block,
        # but the block order is already fixed by higher bits.
        blocks = [nums]
        power = []
        for bit in range(14, -1, -1):
            total = 0
            for idx, blk in enumerate(blocks):
                ones = [x for x in blk if (x >> bit) & 1]
                total += len(ones)
                if len(ones) == len(blk):
                    continue  # whole block has the bit, the prefix keeps going
                if ones:
                    zeros = [x for x in blk if not (x >> bit) & 1]
                    blocks[idx:idx + 1] = [ones, zeros]
                break
            power.append(total)
        return power