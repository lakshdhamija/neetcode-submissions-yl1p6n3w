class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        res, cache = 0, {}
        def dfs(i):
            if i == len(s): return 1
            if i in cache: return cache[i]
            total = 0
            if s[i] != '0': total += dfs(i + 1)
            if s[i] != '0' and i + 1 < len(s) and int(s[i:i+2]) <= 26:
                total += dfs(i + 2)
            cache[i] = total
            return cache[i]
        return dfs(0)