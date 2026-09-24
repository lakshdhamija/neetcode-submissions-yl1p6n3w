class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, amt):
            if amt == 0: return 0
            if amt < 0 or i >= len(coins): return float('inf')
            if (i, amt) in cache: return cache[(i, amt)]
            notInclude = dfs(i + 1, amt)
            include = 1 + dfs(i, amt - coins[i])
            cache[(i, amt)] = min(notInclude, include)
            return cache[(i, amt)]
        op = dfs(0, amount)
        return op if op != float('inf') else -1
            