# Problem: Max Sum of Rectangle No Larger Than K
# Difficulty: Hard
# URL: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# Runtime: 4812 ms
# Memory: 13.1 MB

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        from sortedcontainers import SortedList
        
        m, n = len(matrix), len(matrix[0])
        result = float('-inf')
        
        # Iterate over all pairs of columns
        for left in range(n):
            row_sum = [0] * m
            
            for right in range(left, n):
                # Add column right to row_sum
                for row in range(m):
                    row_sum[row] += matrix[row][right]
                
                # Find max subarray sum <= k using SortedList
                sl = SortedList([0])
                prefix = 0
                
                for s in row_sum:
                    prefix += s
                    # Find smallest x in sl such that prefix - x <= k
                    # i.e., x >= prefix - k
                    idx = sl.bisect_left(prefix - k)
                    if idx < len(sl):
                        result = max(result, prefix - sl[idx])
                    sl.add(prefix)
        
        return result