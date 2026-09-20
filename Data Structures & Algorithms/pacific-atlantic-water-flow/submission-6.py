class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS, dirs, pacific, atlantic = len(heights), len(heights[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]], set(), set()
        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or heights[r][c] < prevHeight: return
            visit.add((r, c))
            for dr, dc in dirs: dfs(r + dr, c + dc, visit, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pacific, float('-inf'))
            dfs(ROWS - 1, c, atlantic, float('-inf'))
        for r in range(ROWS):
            dfs(r, 0, pacific, float('-inf'))
            dfs(r, COLS - 1, atlantic, float('-inf'))
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic: res.append((r, c))
        return res