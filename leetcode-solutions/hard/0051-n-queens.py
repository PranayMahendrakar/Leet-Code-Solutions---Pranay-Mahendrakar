# Problem: N-Queens
# Difficulty: Hard
# URL: https://leetcode.com/problems/n-queens/
# Runtime: 11 ms
# Memory: 12.6 MB

class Solution(object):
    def solveNQueens(self, n):
        result = []
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        board = [['.'] * n for _ in range(n)]
        
        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'
                
                backtrack(row + 1)
                
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'
        
        backtrack(0)
        return result