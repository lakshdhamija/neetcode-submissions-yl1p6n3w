"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            prevStart, prevEnd = intervals[i - 1].start, intervals[i - 1].end
            if start >= prevStart and start < prevEnd: return False
        return True