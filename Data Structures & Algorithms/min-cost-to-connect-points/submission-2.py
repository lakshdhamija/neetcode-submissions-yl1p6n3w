class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i: set() for i in range(n) }
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].add((j, dist))
                adj[j].add((i, dist))
        minHeap, visit, res = [(0, 0)], set(), 0 # [dist, point]
        while minHeap:
            dist, i = heapq.heappop(minHeap)
            if i in visit: continue
            res += dist
            visit.add(i)
            for nei, neiCost in adj[i]:
                if nei not in visit: heapq.heappush(minHeap, (neiCost, nei))
        return res