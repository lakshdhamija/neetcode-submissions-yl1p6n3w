class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]: return nums[l]
            mid = (l + r) // 2
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]: return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]: return nums[mid]
            elif nums[l] < nums[mid]: l = mid + 1
            else: r = mid - 1