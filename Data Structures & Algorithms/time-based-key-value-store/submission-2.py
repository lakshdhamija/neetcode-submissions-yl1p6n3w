class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: self.timeMap[key] = []
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap: return ''
        arr, l, r, res = self.timeMap[key], 0, len(self.timeMap[key]) - 1, ''
        while l <= r: 
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else: r = mid - 1
        return res
