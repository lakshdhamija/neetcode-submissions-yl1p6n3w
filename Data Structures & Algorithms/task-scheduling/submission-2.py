class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        strMap, time, maxHeap, q = {}, 0, [], deque()
        for task in tasks: strMap[task] = strMap.get(task, 0) + 1
        for freq in strMap.values(): heapq.heappush(maxHeap, -freq)
        while maxHeap or q:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 != 0: q.append((time + n, freq + 1))
            else: time = q[0][0]
            if q and q[0][0] == time:
                time, freq = q.popleft()
                heapq.heappush(maxHeap, freq)
        return time