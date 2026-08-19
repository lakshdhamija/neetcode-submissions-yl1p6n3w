class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output, heap = [], []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i + 1 >= k: # valid size
                while heap[0][1] < i - k + 1: heapq.heappop(heap)
                output.append(-heap[0][0])
        return output