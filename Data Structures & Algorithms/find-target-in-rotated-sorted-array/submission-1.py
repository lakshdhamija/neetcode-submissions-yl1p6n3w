class Solution:
    def binarySearch(self, nums, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r, k = 0, len(nums) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            print(mid, nums[mid])
            if nums[mid] == target: return mid
            if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                k = mid
                break
            elif nums[0] <= nums[mid]: l = mid + 1 # we are in left sorted half and pivot is on the right
            else: r = mid - 1 # we are in right sorted half
        print("<<", k)
        leftAns = self.binarySearch(nums, 0, k, target)
        if leftAns != -1: return leftAns
        rightAns = self.binarySearch(nums,k + 1, len(nums) - 1, target)
        if rightAns != -1: return rightAns
        return -1
