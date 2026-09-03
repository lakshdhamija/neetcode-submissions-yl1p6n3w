class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(amt):
            if amt == 0: return 0
            if amt < 0: return -1
            if amt in cache: return cache[amt]
            res = float('inf')
            for coin in coins: 
                if coin <= amt:
                    res = min(res, 1 + dfs(amt - coin))
            cache[amt] = res
            return res
        op = dfs(amount)
        return op if op != float('inf') else -1