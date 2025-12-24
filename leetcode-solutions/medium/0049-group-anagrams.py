# Problem: Group Anagrams
# Difficulty: Medium
# URL: https://leetcode.com/problems/group-anagrams/
# Runtime: 16 ms
# Memory: 16 MB

class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        anagrams = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())