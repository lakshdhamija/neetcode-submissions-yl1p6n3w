class Solution:
    def binarySearch(self, l, r, nums, target):
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
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                pivot = mid
                break
            if nums[l] < nums[mid]: l = mid + 1
            else: r = mid - 1
        print(pivot)
        idx = self.binarySearch(0, pivot, nums, target)
        if idx == -1:
            idx = self.binarySearch(pivot + 1, len(nums) - 1, nums, target)
        return idx