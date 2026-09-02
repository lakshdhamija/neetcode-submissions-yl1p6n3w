class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, res = set(), 0
        for num in nums: numsSet.add(num)
        for num in nums:
            if num - 1 not in numsSet: # possible start
                curLen, curr = 0, num
                while curr in numsSet:
                    curLen += 1
                    curr += 1
                res = max(res, curLen)
        return res