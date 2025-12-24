# Problem: Two Best Non-Overlapping Events
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-best-non-overlapping-events/
# Runtime: 310 ms
# Memory: 46 MB

class Solution:
    def maxTwoEvents(self, events):
        import bisect
        events.sort(key=lambda e: e[1])
        n = len(events)
        max_val = [0] * n
        max_val[0] = events[0][2]
        for i in range(1, n):
            max_val[i] = max(max_val[i-1], events[i][2])
        result = max_val[n-1]
        end_times = [e[1] for e in events]
        for i in range(n):
            start = events[i][0]
            idx = bisect.bisect_left(end_times, start) - 1
            if idx >= 0:
                result = max(result, events[i][2] + max_val[idx])
        return result