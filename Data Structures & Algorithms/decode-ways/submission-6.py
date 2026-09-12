class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        cache = {}
        def dfs(i):
            if i == len(s): return 1
            if i > len(s) or s[i] == '0': return 0
            if i in cache: return cache[i]
            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <=26: res += dfs(i + 2)
            cache[i] = res
            return cache[i]
        return dfs(0)
