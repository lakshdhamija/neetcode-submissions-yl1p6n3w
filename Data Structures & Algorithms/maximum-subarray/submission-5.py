class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = nums[0], 0
        for num in nums:
            curSum += num
            res = max(res, curSum)
            if curSum < 0: curSum = 0
        return res