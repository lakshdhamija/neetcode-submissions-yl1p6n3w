class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum = sum(nums)
        if totSum % 2 != 0: return False
        cache = {}
        def dfs(i, tgt):
            if i >= len(nums) or tgt < 0:
                cache[(i, tgt)] = False
                return False
            if tgt == 0:
                cache[(i, tgt)] = True
                return True
            if (i, tgt) in cache: return cache[(i, tgt)]
            cache[(i, tgt)] = dfs(i + 1, tgt) or dfs(i + 1, tgt - nums[i])
            return cache[(i, tgt)]
        return dfs(0, totSum // 2)