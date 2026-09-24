class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = {}
        def dfs(i, newNums):
            if i >= len(newNums): return 0
            if i in cache: return cache[i]
            rob = newNums[i] + dfs(i + 2, newNums)
            notRob = dfs(i + 1, newNums)
            cache[i] = max(rob, notRob)
            return cache[i]
        robFirst = dfs(0, nums[0: -1])
        cache = {}
        notRobFirst = dfs(0, nums[1:])
        return max(robFirst, notRobFirst)
