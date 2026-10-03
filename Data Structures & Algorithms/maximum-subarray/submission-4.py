class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curSum = nums[0], 0
        for num in nums:
            curSum += num
            res = max(curSum, res)
            curSum = 0 if curSum < 0 else curSum
        return res