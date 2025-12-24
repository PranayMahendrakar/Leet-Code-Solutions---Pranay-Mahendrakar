# Problem: Russian Doll Envelopes
# Difficulty: Hard
# URL: https://leetcode.com/problems/russian-doll-envelopes/
# Runtime: 220 ms
# Memory: 50.8 MB

class Solution:
    def maxEnvelopes(self, envelopes):
        import bisect
        
        # Sort by width ascending, then by height descending
        # This ensures we can't use two envelopes with same width
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # LIS on heights using binary search
        dp = []
        for _, h in envelopes:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        
        return len(dp)