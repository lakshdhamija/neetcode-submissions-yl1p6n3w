"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not len(intervals): return 0
        starts, ends = [], []
        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        count, res = 0, 1
        startI, endI = 0, 0
        while startI < len(intervals) and endI < len(intervals):
            if starts[startI] < ends[endI]:
                count += 1
                startI += 1
                res = max(res, count)
            else:
                count -= 1
                endI += 1
        return res


