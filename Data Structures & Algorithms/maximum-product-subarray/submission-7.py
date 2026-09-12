class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMax, curMin = float('-inf'), 1, 1
        for num in nums:
            temp = curMax
            curMax = max(temp * num, curMin * num, num)
            curMin = min(temp * num, curMin * num, num)
            res = max(res, curMax)
        return res