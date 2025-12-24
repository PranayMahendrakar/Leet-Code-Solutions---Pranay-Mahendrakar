# Problem: Word Search II
# Difficulty: Hard
# URL: https://leetcode.com/problems/word-search-ii/
# Runtime: 889 ms
# Memory: 14 MB

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word  # Mark end of word
        
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(i, j, node):
            char = board[i][j]
            if char not in node:
                return
            
            next_node = node[char]
            
            # Found a word
            if '$' in next_node:
                result.append(next_node['$'])
                del next_node['$']  # Remove to avoid duplicates
            
            # Mark visited
            board[i][j] = '#'
            
            # Explore neighbors
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, next_node)
            
            # Restore
            board[i][j] = char
            
            # Optimization: prune empty branches
            if not next_node:
                del node[char]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        
        return result