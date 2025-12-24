# Problem: Insert Interval
# Difficulty: Medium
# URL: https://leetcode.com/problems/insert-interval/
# Runtime: 4 ms
# Memory: 14.2 MB

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result