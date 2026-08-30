class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMin, curMax = max(nums), 1, 1
        for num in nums:
            tmp = curMax
            curMax = max(num * tmp, num * curMin, num)
            curMin = min(num * tmp, num * curMin, num)
            # print(num, curMin, curMax, res)
            res = max(res, curMax, curMin)
        return res
