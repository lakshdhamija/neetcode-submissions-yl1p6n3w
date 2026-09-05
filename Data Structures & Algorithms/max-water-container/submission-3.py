class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, maxArea = 0, len(heights) - 1, 0
        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))
            if heights[r] < heights[l]: r -= 1
            else: l += 1
        return maxArea