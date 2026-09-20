class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap, heap, q, maxFreq = {}, [], deque(), 0
        for c in s:
            countMap[c] = countMap.get(c, 0) + 1
            maxFreq = max(maxFreq, countMap[c])
        # if maxFreq > math.ceil(len(s) / 2): return ''
        for c, f in countMap.items(): heapq.heappush(heap, (-f, c))
        res = []
        while heap or q:
            if heap:
                f, c = heapq.heappop(heap)
                if res and res[-1] == c:
                    if not heap: return '' # we cant append the same char and no more left
                    f2, c2 = heapq.heappop(heap)
                    res.append(c2)
                    if f2 + 1 != 0: heapq.heappush(heap, (f2 + 1, c2))
                    heapq.heappush(heap, (f, c))
                else:
                    res.append(c)
                    if f + 1 != 0: heapq.heappush(heap, (f + 1, c))
        return ''.join(res)