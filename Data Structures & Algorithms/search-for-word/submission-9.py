class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs, ROWS, COLS, visit, i = [[1, 0], [-1, 0], [0, 1], [0, -1]], len(board), len(board[0]), set(), 0
        def dfs(r, c):
            nonlocal i
            if i == len(word): return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] != word[i]: return False
            visit.add((r, c))
            res = False
            i += 1
            for dr, dc in dirs:
                res = res or dfs(r + dr, c + dc)
            visit.remove((r, c))
            i -= 1
            return res
        for r in range(ROWS):
            for c in range(COLS): 
                if board[r][c] == word[0]:
                    if dfs(r, c): return True
        return False
