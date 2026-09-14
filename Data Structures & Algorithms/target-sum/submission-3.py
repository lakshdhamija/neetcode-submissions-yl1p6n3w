class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, sm):
            if sm == target and i == len(nums): return 1
            if i >= len(nums): return 0
            if (i, sm) in cache: return cache[(i, sm)]
            ways = 0
            ways += dfs(i + 1, sm + nums[i])
            ways += dfs(i + 1, sm - nums[i])
            cache[(i, sm)] = ways
            return ways
        return dfs(0, 0)