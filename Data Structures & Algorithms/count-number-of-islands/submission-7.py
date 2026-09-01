class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS, dirs = len(grid), len(grid[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
 
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        return res