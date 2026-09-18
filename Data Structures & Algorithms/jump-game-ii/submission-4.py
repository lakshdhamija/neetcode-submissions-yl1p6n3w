class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i == len(nums) - 1: return 0
            if i >= len(nums): return float('inf')
            if i in cache: return cache[i]
            res = float('inf')
            for j in range(nums[i]):
                res = min(res, 1 + dfs(i + j + 1))
            cache[i] = res
            return res
        return dfs(0)