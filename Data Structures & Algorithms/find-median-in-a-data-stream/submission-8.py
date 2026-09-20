class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if self.right and num >= self.right[0]: heapq.heappush(self.right, num)
        else: heapq.heappush(self.left, -num)
        if len(self.right) - len(self.left) >= 2:
            n = heapq.heappop(self.right)
            heapq.heappush(self.left, -n)
        elif len(self.left) - len(self.right) >= 2:
            n = heapq.heappop(self.left)
            heapq.heappush(self.right, -n)

    def findMedian(self) -> float:
        if not self.right: return -self.left[0]
        if (len(self.left) + len(self.right)) % 2:
            return (-self.left[0]) if len(self.left) > len(self.right) else self.right[0]
        else: return (-self.left[0] + self.right[0]) / 2
        