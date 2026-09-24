class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, j):
            if i == len(nums): return 0
            if (i, j) in cache: return cache[(i, j)]
            LIS = dfs(i + 1, j)
            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            cache[(i, j)] = LIS
            return cache[(i, j)]
        return dfs(0, -1)