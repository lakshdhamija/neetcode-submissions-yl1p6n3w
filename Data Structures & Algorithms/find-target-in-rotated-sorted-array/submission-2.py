class Solution:
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r, pivot = 0, len(nums) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                pivot = mid
                break
            elif nums[l] < nums[mid]: l = mid + 1
            else: r = mid - 1
        targetInLeft = self.binarySearch(nums, 0, pivot, target)
        if targetInLeft != -1: return targetInLeft
        return self.binarySearch(nums, pivot + 1, len(nums) - 1, target)