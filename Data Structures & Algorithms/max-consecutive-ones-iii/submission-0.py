class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, res, numZeros = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 1: res = max(res, r - l + 1)
            else:
                numZeros += 1
                while numZeros > k: 
                    if nums[l] == 0: numZeros -= 1
                    l += 1
                res = max(res, r - l + 1)
            r += 1
        return res
