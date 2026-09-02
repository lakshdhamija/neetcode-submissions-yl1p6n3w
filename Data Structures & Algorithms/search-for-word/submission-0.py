class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, path, dirs = len(board), len(board[0]), set(), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or word[i] != board[r][c]: return False
            path.add((r, c))
            res = False
            for dr, dc in dirs: res = res or dfs(r + dr, c + dc, i + 1)
            path.remove((r, c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if (dfs(r, c, 0)): return True
        return False