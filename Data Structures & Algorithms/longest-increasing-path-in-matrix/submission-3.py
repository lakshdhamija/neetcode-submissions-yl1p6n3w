class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs, ROWS, COLS, visit, cache = [[1, 0], [-1, 0], [0, 1], [0, -1]], len(matrix), len(matrix[0]), set(), {}
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or matrix[r][c] <= prev: return 0
            if (r, c) in cache: return cache[(r, c)]
            visit.add((r, c))
            res = 0
            for dr, dc in dirs:
                res = max(res, 1 + dfs(r + dr, c + dc , matrix[r][c]))
            visit.remove((r, c))
            cache[(r, c)] = res
            return res
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        return res