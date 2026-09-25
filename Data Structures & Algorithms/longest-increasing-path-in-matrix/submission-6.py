class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS, dirs, res = len(matrix), len(matrix[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]], 0
        cache = {}
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev: return 0
            if (r, c) in cache: return cache[(r, c)]
            res = 1
            for dr, dc in dirs: res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            cache[(r, c)] = res
            return res
        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float('-inf')))
        return LIP
            
