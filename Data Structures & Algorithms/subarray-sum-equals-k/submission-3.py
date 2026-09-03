class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curSum, prefixSum = 0, 0, { 0: 1 }
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefixSum: res += prefixSum[diff]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res