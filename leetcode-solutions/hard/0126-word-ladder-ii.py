# Problem: Word Ladder II
# Difficulty: Hard
# URL: https://leetcode.com/problems/word-ladder-ii/
# Runtime: 32 ms
# Memory: 13 MB

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict, deque
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Build graph and find shortest path using BFS
        # Track parents for each word to reconstruct paths
        layer = {beginWord}
        parents = defaultdict(set)
        
        while layer and endWord not in layer:
            next_layer = set()
            wordSet -= layer  # Remove visited words
            
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_layer.add(new_word)
                            parents[new_word].add(word)
            
            layer = next_layer
        
        # Reconstruct all shortest paths using DFS
        result = []
        
        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                backtrack(parent, path + [parent])
        
        if endWord in parents:
            backtrack(endWord, [endWord])
        
        return result