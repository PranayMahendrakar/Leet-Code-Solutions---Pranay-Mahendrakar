class Solution(object):
    def longestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        first = [-1] * k
        first[0] = 0

        # Prefix remainders in order of first appearance.
        order = [0]

        # Number of remainders already processed for each shift.
        processed = [0] * k

        # Earliest valid start for each ending remainder,
        # using one negation encountered so far.
        best_flip = [len(nums) + 1] * k

        prefix = 0
        answer = 0

        for right, x in enumerate(nums, 1):
            shift = (2 * x) % k
            count = len(order)

            for j in range(processed[shift], count):
                remainder = order[j]
                target = remainder + shift
                if target >= k:
                    target -= k

                start = first[remainder]
                if start < best_flip[target]:
                    best_flip[target] = start

            processed[shift] = count
            prefix = (prefix + x) % k

            # No negation.
            if first[prefix] != -1:
                answer = max(answer, right - first[prefix])

            # One negation.
            answer = max(answer, right - best_flip[prefix])

            # Register after processing x so x lies within
            # every subarray considered above.
            if first[prefix] == -1:
                first[prefix] = right
                order.append(prefix)

        return answer