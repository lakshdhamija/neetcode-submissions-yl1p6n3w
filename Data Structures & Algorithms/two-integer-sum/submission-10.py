class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            toFind = target - num
            if toFind in numMap: return [numMap[toFind], i]
            else: numMap[num] = i
        return []
