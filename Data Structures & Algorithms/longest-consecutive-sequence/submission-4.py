class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums: numSet.add(num)
        res = 0
        for num in numSet:
            if num - 1 not in numSet: 
                curLen, curr = 1, num
                while curr + 1 in numSet:
                    curLen += 1
                    curr += 1
                res = max(res, curLen)
        return res

