class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numMap = {}
        # for i, num in enumerate(nums):
        #     numToFind = target - num
        #     if numToFind in numMap: return [numMap[numToFind], i]
        #     else: numMap[num] = i
        # return []
        numMap = {}
        for i, num in enumerate(nums): numMap[num] = i
        for i, num in enumerate(nums):
            numToFind = target - num
            if numToFind in numMap and numMap[numToFind] != i: return [i, numMap[numToFind]]
        return []