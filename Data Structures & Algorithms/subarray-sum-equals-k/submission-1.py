class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = { 0 : 1 }
        for num in nums: 
            curSum += num
            diff = curSum - k # if we can a prefix array with sum == diff, then we do have a contiguous array that can sums upto k
            if diff in prefixSum: res += prefixSum[diff]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res