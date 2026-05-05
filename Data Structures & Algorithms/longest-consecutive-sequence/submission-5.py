class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            length = 1
            if num - 1 not in numSet:
                curr = num
                while curr + 1 in numSet:
                    length += 1
                    curr += 1
                res = max(res, length)
        return res