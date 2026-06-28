class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums: count[num] = count.get(num, 0) + 1
        # pq = []
        # for num, freq in count.items():
        #     heapq.heappush(pq, [freq, num])
        #     if len(pq) > k: heapq.heappop(pq)
        # res = []
        # for i in range(k): res.append(heapq.heappop(pq)[1])
        # return res
        buckets = [[] for _ in range(len(nums) + 1)]
        freqMap = {}
        for num in nums: freqMap[num] = freqMap.get(num, 0) + 1
        for key, v in freqMap.items(): buckets[v].append(key)
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k: return output
        return output