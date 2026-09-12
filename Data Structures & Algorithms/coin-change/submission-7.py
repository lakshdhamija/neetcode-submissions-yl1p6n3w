class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, amount):
            if amount < 0 or i >= len(coins): return float('inf')
            if amount == 0: return 0
            if (i, amount) in cache: return cache[(i, amount)]
            notInclude = dfs(i + 1, amount)
            include = 1 + dfs(i, amount - coins[i])
            cache[(i, amount)] = min(notInclude, include)
            return cache[(i, amount)]
        minCoins = dfs(0, amount)
        return minCoins if minCoins != float('inf') else -1
