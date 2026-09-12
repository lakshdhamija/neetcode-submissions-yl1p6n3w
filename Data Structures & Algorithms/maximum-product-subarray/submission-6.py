class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, maxPro, minPro = float('-inf'), 1, 1
        for num in nums:
            tmp = maxPro
            maxPro = max(tmp * num, minPro * num, num)
            minPro = min(tmp * num, minPro * num, num)
            res = max(maxPro, res)
        return res
        