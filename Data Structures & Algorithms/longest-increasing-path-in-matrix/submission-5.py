class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs, ROWS, COLS, cache = [[1, 0], [-1, 0], [0, 1], [0, -1]], len(matrix), len(matrix[0]), {}
        def dfs(r, c):
            if (r, c) in cache: return cache[(r, c)]
            res = 1
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or matrix[nr][nc] <= matrix[r][c]: continue
                res = max(res, 1 + dfs(r + dr, c + dc))
            cache[(r, c)] = res
            return res
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res