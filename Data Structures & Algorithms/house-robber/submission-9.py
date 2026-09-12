class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)
        zero, one = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            two = max(one, zero + nums[i])
            zero, one = one, two
        return one