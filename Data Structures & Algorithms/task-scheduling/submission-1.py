class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        strMap, time, maxHeap, q = {}, 0, [], deque()
        for task in tasks: strMap[task] = strMap.get(task, 0) + 1
        for task, freq in strMap.items(): heapq.heappush(maxHeap, (-freq, task))
        while maxHeap or q:
            time += 1
            if maxHeap:
                freq, task = heapq.heappop(maxHeap)
                if freq + 1 != 0: q.append((time + n, freq + 1, task))
            if q and q[0][0] == time:
                time, freq, task = q.popleft()
                heapq.heappush(maxHeap, (freq, task))
        return time