class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charLastIdx = {}
        for i, c in enumerate(s): charLastIdx[c] = i
        res, size, end = [], 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, charLastIdx[c])
            if i == end:
                res.append(size)
                size = 0
        return res