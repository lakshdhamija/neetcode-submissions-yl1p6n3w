class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        if nums[0] == target and nums[-1] == target: return [0, len(nums) - 1]
        l, r, start = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0:
                    start = 0
                    break
                if nums[mid - 1] == nums[mid]: r = mid - 1 #starting is still on the left
                else:
                    start = mid
                    break
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1

        l, r, end = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    end = len(nums) - 1
                    break
                if nums[mid + 1] == nums[mid]: l = mid + 1 #ending point is still on the right
                else:
                    end = mid
                    break
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return [start, end]