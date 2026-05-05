class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: count[num] = count.get(num, 0) + 1
        pq = []
        for num, freq in count.items():
            heapq.heappush(pq, [freq, num])
            if len(pq) > k: heapq.heappop(pq)
        res = []
        for i in range(k): res.append(heapq.heappop(pq)[1])
        return res