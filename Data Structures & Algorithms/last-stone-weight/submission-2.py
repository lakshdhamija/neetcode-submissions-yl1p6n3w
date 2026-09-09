class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        heap = []
        for stone in stones: heapq.heappush(heap, -stone)
        while len(heap) > 1:
            one, two = -heapq.heappop(heap), -heapq.heappop(heap)
            diff = abs(one - two)
            if diff == 0: continue
            heapq.heappush(heap, -diff)
        return -heap[0] if heap else 0
