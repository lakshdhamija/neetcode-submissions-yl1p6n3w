class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            target = 0 - num
            if i > 0 and nums[i - 1] == nums[i]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target: r -= 1
                elif nums[l] + nums[r] < target: l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    # while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
        return res