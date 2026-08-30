class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        r, curSum = 0, 0
        while r < len(nums):
            curSum += nums[r]
            res = max(curSum, res)
            if curSum < 0: curSum = 0
            r += 1
        return res
        