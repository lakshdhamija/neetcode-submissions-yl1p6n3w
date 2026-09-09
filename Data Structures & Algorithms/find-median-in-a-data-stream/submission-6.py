class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num: heapq.heappush(self.minHeap, num)
        else: heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) - len(self.maxHeap) >= 2:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) >= 2:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else: return -self.maxHeap[0]
        