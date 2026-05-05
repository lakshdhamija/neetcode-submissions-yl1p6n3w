class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, leftMax, rightMax, res = 0, len(height) - 1, height[0], height[len(height) - 1], 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res