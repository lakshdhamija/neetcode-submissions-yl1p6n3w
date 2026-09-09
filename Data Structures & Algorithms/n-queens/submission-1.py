class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board = [], [["."]*n for _ in range(n)]
        col, posDiag, negDiag = set(), set(), set()
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board] 
                res.append(copy)
                return
            for c in range(n): # iterating every column
                if c in col or (r + c) in posDiag or (r - c) in negDiag: continue
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                dfs(r + 1)
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        dfs(0)
        return res