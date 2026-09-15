class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        prevEnd, res = intervals[0][1], 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd: # overlap
                res += 1
                prevEnd = min(prevEnd, end)
            else: prevEnd = end
        return res