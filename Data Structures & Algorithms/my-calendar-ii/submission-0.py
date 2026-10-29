class MyCalendarTwo:
    
    def __init__(self):
        self.overlapEvents = []
        self.nonOverlapEvents = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.overlapEvents:
            if startTime < end and endTime > start: return False
        for start, end in self.nonOverlapEvents:
            if startTime < end and endTime > start:
                self.overlapEvents.append((max(start, startTime), min(end, endTime)))
        self.nonOverlapEvents.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)