from bisect import bisect_left


class Solution(object):
    def countIntersectingIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        ends = sorted(e for _, e in intervals)
        # a pair is disjoint exactly when one interval ends before the other starts
        disjoint = sum(bisect_left(ends, s) for s, _ in intervals)
        return n * (n - 1) // 2 - disjoint