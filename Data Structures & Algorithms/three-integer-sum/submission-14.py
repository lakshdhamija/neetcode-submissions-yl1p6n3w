class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, i = [], 0
        print(nums)
        while i < len(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                diff = 0 - nums[i]
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]: l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < diff:
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]: l += 1
                    l += 1
                else:
                    while r - 1 > l and nums[r] == nums[r - 1]: r -= 1
                    r -= 1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: i += 1
            i += 1
        return res
