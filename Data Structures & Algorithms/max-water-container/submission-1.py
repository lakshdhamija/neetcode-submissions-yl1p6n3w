class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, res = 0, len(heights) - 1, 0
        while l < r:
            leftH, rightH = heights[l], heights[r]
            res = max(res, min(leftH, rightH) * (r - l))
            if leftH <= rightH: l += 1
            else: r -= 1
        return res