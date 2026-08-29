class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(step):
            if step <= 2: return step
            if step in memo: return memo[step]
            memo[step] = dfs(step - 1) + dfs(step - 2)
            return memo[step]
        return dfs(n)