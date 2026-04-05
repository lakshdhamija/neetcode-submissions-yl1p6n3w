class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, res = [0] * len(height), [0] * len(height), 0
        maxLeft[0], maxRight[len(height) - 1] = height[0], height[len(height) - 1]
        for i in range(1, len(height)): maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1): maxRight[i] = max(maxRight[i + 1], height[i])
        for i in range(len(height)): res += min(maxLeft[i], maxRight[i]) - height[i]
        return res
            