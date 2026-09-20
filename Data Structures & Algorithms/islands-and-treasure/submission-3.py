class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, q, dirs = len(grid), len(grid[0]), deque(), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: q.append((r, c))
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647: continue
                    grid[nr][nc] = level
                    q.append((nr, nc))
                