class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        cache = {}
        def dfs(i, m):
            if i == len(nums): return 0 if m == 0 else float('inf')
            if m == 0: return float('inf')
            if (i, m) in cache: return cache[(i, m)]
            res, curSum = float('inf'), 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))
            cache[(i, m)] = res
            return cache[(i, m)]
        return dfs(0, k)