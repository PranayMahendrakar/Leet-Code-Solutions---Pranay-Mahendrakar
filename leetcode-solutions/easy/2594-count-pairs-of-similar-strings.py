# Problem: Count Pairs Of Similar Strings
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-pairs-of-similar-strings/
# Runtime: 24 ms
# Memory: 12.7 MB

class Solution(object):
    def similarPairs(self, words):
        from collections import Counter
        signatures = [frozenset(word) for word in words]
        count = 0
        n = len(signatures)
        for i in range(n):
            for j in range(i + 1, n):
                if signatures[i] == signatures[j]:
                    count += 1
        return count