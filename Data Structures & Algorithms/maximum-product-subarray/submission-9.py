class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minPro, maxPro, res = 1, 1, float('-inf')
        for num in nums:
            temp = maxPro
            maxPro = max(temp * num, minPro * num, num)
            minPro = min(temp * num, minPro * num, num)
            res = max(res, maxPro)
        return res