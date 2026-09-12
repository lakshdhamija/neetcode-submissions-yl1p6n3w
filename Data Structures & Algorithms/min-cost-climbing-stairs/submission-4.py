class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1) # dp[i] = minimum cost to reach step i
        # we can start at 0 or 1 for free, i.e., 0 cost needed to reach those.
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]) # we can reach i from i - 2 or i - 1
        return dp[len(cost)]