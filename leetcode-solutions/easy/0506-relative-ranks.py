# Problem: Relative Ranks
# Difficulty: Easy
# URL: https://leetcode.com/problems/relative-ranks/
# Runtime: 4 ms
# Memory: 13.2 MB

class Solution(object):
    def findRelativeRanks(self, score):
        sorted_idx = sorted(range(len(score)), key=lambda i: -score[i])
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * len(score)
        for i, idx in enumerate(sorted_idx):
            result[idx] = medals[i] if i < 3 else str(i + 1)
        return result