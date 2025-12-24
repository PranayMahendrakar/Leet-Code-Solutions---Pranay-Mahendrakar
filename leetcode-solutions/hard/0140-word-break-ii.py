# Problem: Word Break II
# Difficulty: Hard
# URL: https://leetcode.com/problems/word-break-ii/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [[]]
            
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for rest in backtrack(end):
                        result.append([word] + rest)
            
            memo[start] = result
            return result
        
        return [' '.join(words) for words in backtrack(0)]