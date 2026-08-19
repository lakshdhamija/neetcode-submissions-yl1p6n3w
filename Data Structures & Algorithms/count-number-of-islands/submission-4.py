class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        def dfs(r: int, c: int):
            if (r, c) in visit or r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]): return
            visit.add((r,c))
            if grid[r][c] == '1': grid[r][c] = '0'
            else: return
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            visit.remove((r,c))
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == '1'):
                    res += 1
                    dfs(r, c)
        return res


