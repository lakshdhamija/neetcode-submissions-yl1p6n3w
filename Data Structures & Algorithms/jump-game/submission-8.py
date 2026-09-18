class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i >= len(nums) - 1: return True
            if i in cache: return cache[i]
            res = False
            for j in range(nums[i]):
                res = res or dfs(i + j + 1)
            cache[i] = res
            return res
        return dfs(0)