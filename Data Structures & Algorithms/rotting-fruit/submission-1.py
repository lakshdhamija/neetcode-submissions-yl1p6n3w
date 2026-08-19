class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, time, fresh, ROWS, COLS, directions = deque(), 0, 0, len(grid), len(grid[0]), [[1,0], [-1,0], [0,1], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: fresh += 1
                if grid[r][c] == 2: q.append((r, c))
        while q and fresh > 0:
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1: continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
        return time if fresh == 0 else -1
        
        