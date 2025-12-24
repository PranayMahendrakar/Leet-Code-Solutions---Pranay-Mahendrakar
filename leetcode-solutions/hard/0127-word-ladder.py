# Problem: Word Ladder
# Difficulty: Hard
# URL: https://leetcode.com/problems/word-ladder/
# Runtime: 39 ms
# Memory: 12.9 MB

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # Bidirectional BFS for optimal time complexity
        front = {beginWord}
        back = {endWord}
        wordSet.discard(beginWord)
        
        length = 1
        
        while front and back:
            # Always expand the smaller set
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in back:
                            return length + 1
                        if new_word in wordSet:
                            next_front.add(new_word)
                            wordSet.remove(new_word)
            
            front = next_front
            length += 1
        
        return 0