class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        rob0, rob1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)): rob0, rob1 = rob1, max(rob1, nums[i] + rob0)
        return rob1