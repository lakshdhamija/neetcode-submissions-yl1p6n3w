class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i > len(cost): return float('inf')
            if i == len(cost): return 0 # reached last floor
            if i in cache: return cache[i]
            climbOneFloorCost = cost[i] + dfs(i + 1)
            climbTwoFloorCost = cost[i] + dfs(i + 2)
            cache[i] = min(climbOneFloorCost, climbTwoFloorCost)
            return cache[i]
        return min(dfs(0), dfs(1))