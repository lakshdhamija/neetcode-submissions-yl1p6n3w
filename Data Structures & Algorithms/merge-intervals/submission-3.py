class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [[intervals[0][0], intervals[0][1]]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            currStart, currEnd = res[-1][0], res[-1][1]
            if start >= currStart and start <= currEnd: # overlap
                newInterval = [min(currStart, start), max(currEnd, end)]
                res.pop()
                res.append(newInterval)
            else: res.append([start, end])
        return res
