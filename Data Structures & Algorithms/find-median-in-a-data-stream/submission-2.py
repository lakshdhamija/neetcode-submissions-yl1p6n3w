class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        if self.largeHeap and num > self.largeHeap[0]: heapq.heappush(self.largeHeap, num)
        else: heapq.heappush(self.smallHeap, -num)
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            poppedNum = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -poppedNum)
        elif len(self.smallHeap) + 1 < len(self.largeHeap):
            poppedNum = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -poppedNum)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap): return -self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap): return self.largeHeap[0]
        return (-self.smallHeap[0] + (self.largeHeap[0])) / 2.0 # even elements
        
        