class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, visited, dirs = len(board), len(board[0]), set(), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != word[i]: return False
            visited.add((r, c))
            res = False
            for dr, dc in dirs:
                res = res or dfs(dr + r, dc + c, i + 1)
            visited.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
