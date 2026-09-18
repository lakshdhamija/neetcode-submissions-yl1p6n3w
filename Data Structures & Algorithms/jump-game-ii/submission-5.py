class Solution:
    def jump(self, nums: List[int]) -> int:
        res = l = r = 0
        while r < len(nums) - 1:
            nextMax = 0
            for i in range(l, r + 1):
                nextMax = max(nextMax, i + nums[i])
            l = r + 1
            res += 1
            r = nextMax
        return res