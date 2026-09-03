class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS, dirs = len(grid), len(grid[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0': return
            grid[r][c] = '0'
            for dr, dc in dirs: dfs(r + dr, c + dc)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1': 
                    res += 1
                    dfs(r, c)
        return res