class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                if l != i: swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 1: i += 1
            else:
                if i != r: swap(i, r)
                r -= 1

