class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, dirs, visit = len(board), len(board[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]], set()
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] != word[i]: return False
            print(board[r][c])
            visit.add((r, c))
            found = False
            for dr, dc in dirs: found = found or dfs(r + dr, c + dc, i + 1)
            visit.remove((r, c))
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False