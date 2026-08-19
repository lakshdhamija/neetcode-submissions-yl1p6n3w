class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = { 0 : 1 }
        for num in nums: 
            curSum += num
            if curSum - k in prefixSum: res += prefixSum[curSum - k]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res