class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False # cannot have 2 equal parts 
        cache = {}
        def dfs(i, target):
            if target == 0: return True
            if i >= len(nums): return False
            if (i, target) in cache: return cache[(i, target)]
            cache[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return cache[(i, target)]
        return dfs(0, total / 2)
        