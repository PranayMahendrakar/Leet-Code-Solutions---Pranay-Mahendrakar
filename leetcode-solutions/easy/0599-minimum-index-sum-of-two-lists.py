# Problem: Minimum Index Sum of Two Lists
# Difficulty: Easy
# URL: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Runtime: 16 ms
# Memory: 12.6 MB

class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, s in enumerate(list2):
            if s in index_map:
                idx_sum = index_map[s] + j
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [s]
                elif idx_sum == min_sum:
                    result.append(s)
        return result