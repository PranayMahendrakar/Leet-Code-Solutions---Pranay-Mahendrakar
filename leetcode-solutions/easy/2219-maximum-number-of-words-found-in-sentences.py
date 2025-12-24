# Problem: Maximum Number of Words Found in Sentences
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Runtime: 0 ms
# Memory: 12.5 MB

class Solution(object):
    def mostWordsFound(self, sentences):
        return max(sentence.count(' ') + 1 for sentence in sentences)