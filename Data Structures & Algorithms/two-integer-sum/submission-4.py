class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            curNum = nums[i]
            diff = target - curNum
            if diff in numSet:
                return [numSet[diff], i]
            numSet[curNum] = i
