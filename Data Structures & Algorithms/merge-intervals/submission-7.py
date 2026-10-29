class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        returnIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevStart, prevEnd = returnIntervals[-1]
            if start <= prevEnd and end > prevStart:
                returnIntervals[-1] = [min(start, prevStart), max(end, prevEnd)]
            else:
                returnIntervals.append(intervals[i])
        return returnIntervals
            