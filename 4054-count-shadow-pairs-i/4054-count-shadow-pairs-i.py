class Solution(object):
    def shadowPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nxt = [n] * n  # next index to the right with a strictly smaller value
        eq = [0] * n   # equal values between i and nxt[i]
        stack = []
        total = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                top = stack[-1]
                if nums[top] == nums[i]:
                    nxt[i] = nxt[top]
                    eq[i] = eq[top] + 1
                else:
                    nxt[i] = top
            stack.append(i)
            # every j in (i, nxt[i]) has nums[j] >= nums[i]; drop the equal ones
            total += nxt[i] - i - 1 - eq[i]
        return total