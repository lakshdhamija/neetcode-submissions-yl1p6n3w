class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if i == len(nums): return 0
            if (i, prev) in cache: return cache[(i, prev)]
            LIS = dfs(i + 1, prev)
            if nums[i] > prev: LIS = max(LIS, 1 + dfs(i + 1, nums[i]))
            cache[(i, prev)] = LIS
            return LIS
        return dfs(0, float('-inf'))