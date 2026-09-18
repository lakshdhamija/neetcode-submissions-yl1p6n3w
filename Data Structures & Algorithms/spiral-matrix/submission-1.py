class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, top, bottom, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while top <= bottom and l <= r:
            for col in range(l, r + 1):
                res.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                res.append(matrix[row][r])
            r -= 1
            if top <= bottom:
                for col in range(r, l - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            if l <= r:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][l])
                l += 1
        return res