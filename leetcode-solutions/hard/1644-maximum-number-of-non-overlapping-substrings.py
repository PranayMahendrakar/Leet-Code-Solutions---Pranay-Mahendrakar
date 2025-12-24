# Problem: Maximum Number of Non-Overlapping Substrings
# Difficulty: Hard
# URL: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
# Runtime: 263 ms
# Memory: 18.6 MB

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Find first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        # Get the valid interval for each character
        def get_interval(c):
            left, right = first[c], last[c]
            i = left
            while i <= right:
                if first[s[i]] < left:
                    return None  # Can't form valid interval
                right = max(right, last[s[i]])
                i += 1
            return (left, right)
        
        # Get all valid intervals
        intervals = []
        for c in first:
            interval = get_interval(c)
            if interval:
                intervals.append(interval)
        
        # Sort by end position, then by start position descending (to get shortest)
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Greedy selection of non-overlapping intervals
        result = []
        prev_end = -1
        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right+1])
                prev_end = right
        
        return result