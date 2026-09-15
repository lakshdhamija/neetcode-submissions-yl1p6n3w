class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        returnIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            prevStart, prevEnd = returnIntervals[-1]
            start, end = intervals[i]
            if prevStart <= start <= prevEnd:
                returnIntervals.pop()
                returnIntervals.append([min(prevStart, start), max(prevEnd, end)])
            else: returnIntervals.append(intervals[i])
        return returnIntervals
