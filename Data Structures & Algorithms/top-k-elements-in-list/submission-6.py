class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen, pq = {}, []
        for num in nums: seen[num] = seen.get(num, 0) + 1
        for key, val in seen.items():
            heapq.heappush(pq, (val, key))
            if len(pq) > k: heapq.heappop(pq)
        res = []
        for i in range(k): res.append(heapq.heappop(pq)[1])
        return res