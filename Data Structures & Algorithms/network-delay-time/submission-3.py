class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for u, v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append((v, t))
        minHeap, visit, t = [(0, k)], set(), 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit: continue
            visit.add(n1)
            t = max(t, t1)
            if n1 in edges:
                for n2, t2 in edges[n1]:
                    if n2 not in visit: heapq.heappush(minHeap, (t1 + t2, n2))
        return t if len(visit) == n else -1