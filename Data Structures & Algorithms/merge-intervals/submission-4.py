class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = res[-1]
            if start >= prevStart and start <= prevEnd: # overlap so merge
                newStart = min(start, prevStart)
                newEnd = max(end, prevEnd)
                res[-1] = [newStart, newEnd]
            else: res.append(intervals[i])
        return res