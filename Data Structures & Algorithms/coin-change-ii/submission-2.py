class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, amount):
            if amount == 0: return 1
            if amount < 0 or i >= len(coins): return 0
            if (i, amount) in cache: return cache[(i, amount)]
            skipCurrentCoin = dfs(i + 1, amount)
            considerCurrentCoin = dfs(i, amount - coins[i])
            cache[(i, amount)] = skipCurrentCoin + considerCurrentCoin
            return cache[(i, amount)]
        return dfs(0, amount)