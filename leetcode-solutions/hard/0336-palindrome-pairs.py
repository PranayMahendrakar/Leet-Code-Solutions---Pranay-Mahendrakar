# Problem: Palindrome Pairs
# Difficulty: Hard
# URL: https://leetcode.com/problems/palindrome-pairs/
# Runtime: 2665 ms
# Memory: 25.2 MB

class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]
        
        word_map = {w: i for i, w in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            n = len(word)
            
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: prefix is palindrome, check if reverse of suffix exists
                if is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        result.append([word_map[rev_suffix], i])
                
                # Case 2: suffix is palindrome, check if reverse of prefix exists
                if j != n and is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        result.append([i, word_map[rev_prefix]])
        
        return result