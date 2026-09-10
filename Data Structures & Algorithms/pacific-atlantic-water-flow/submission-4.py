class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS, pacific, atlantic, dirs = len(heights), len(heights[0]), set(), set(), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight): return
            visit.add((r, c))
            for dr, dc in dirs: dfs(r + dr, c + dc, visit, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in pacific or (r, c) not in atlantic: continue
                res.append([r, c])
        return res