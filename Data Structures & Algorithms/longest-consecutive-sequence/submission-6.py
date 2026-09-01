class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet, res = set(), 0
        for num in nums: hashSet.add(num)
        for num in nums:
            if num - 1 not in hashSet: # possible start
                curr, curLen = num, 0
                while curr in hashSet:
                    curLen += 1
                    curr = curr + 1
                res = max(res, curLen)
        return res