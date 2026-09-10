class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res, ROWS, COLS, dirs = 0, len(grid), len(grid[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs: area += dfs(r + dr, c + dc)
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res