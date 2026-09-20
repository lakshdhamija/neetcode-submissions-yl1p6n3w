class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap, q, maxHeap, time = {}, deque(), [], 0
        for task in tasks: freqMap[task] = freqMap.get(task, 0) + 1
        for freq in freqMap.values(): heapq.heappush(maxHeap, -freq)
        while q or maxHeap:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 != 0: q.append((time + n, freq + 1))
            else: time = q[0][0]
            if q and q[0][0] == time:
                _, freq = q.popleft()
                heapq.heappush(maxHeap, freq)
        return time
