class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, buying):
            if i >= len(prices): return 0
            if (i, buying) in cache: return cache[(i, buying)]
            skip = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] = max(buy, skip)
                return cache[(i, buying)]
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, skip)
                return cache[(i, buying)]
        return dfs(0, True)