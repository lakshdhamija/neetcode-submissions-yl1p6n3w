class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, visit, minHeap, dirs  = len(grid), set(), [(grid[0][0], 0, 0)], [[1, 0], [-1, 0], [0, 1], [0, -1]]
        print(minHeap)
        while minHeap:
            maxHeight, r, c = heapq.heappop(minHeap)
            if (r, c) in visit: continue
            if r == N - 1 and c == N - 1: return maxHeight
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= N or nc >= N or (nr, nc) in visit: continue
                heapq.heappush(minHeap, (max(maxHeight, grid[nr][nc]), nr, nc))
        return -1 