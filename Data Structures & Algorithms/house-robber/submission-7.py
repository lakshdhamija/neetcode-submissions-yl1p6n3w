class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums): return 0
            if i in cache: return cache[i]
            robCurrentHouse = nums[i] + dfs(i + 2)
            skipCurrentHouse = dfs(i + 1)
            cache[i] = max(robCurrentHouse, skipCurrentHouse)
            return cache[i]
        return dfs(0)