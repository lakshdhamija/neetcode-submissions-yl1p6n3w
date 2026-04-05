class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, leftMax, rightMax, res = 1, len(height) - 2, height[0], height[len(height) - 1], 0
        while l <= r:
            if leftMax < rightMax:
                res += max(0, leftMax - height[l])
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                res += max(0, rightMax - height[r])
                rightMax = max(rightMax, height[r])
                r -= 1
        return res