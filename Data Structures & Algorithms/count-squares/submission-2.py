class CountSquares:

    def __init__(self):
        self.pointCount = {}

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.pointCount[key] = self.pointCount.get(key, 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pointCount:
            if (abs(py - y) != abs(px - x)) or x == px or y == py: continue
            if (x, py) in self.pointCount and (px, y) in self.pointCount:
                res += self.pointCount[(x, py)] * self.pointCount[(px, y)] * self.pointCount[(x, y)]
        return res