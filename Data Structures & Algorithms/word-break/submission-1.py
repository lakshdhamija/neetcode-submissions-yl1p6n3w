class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(i):
            if i == len(s): return True
            if i in cache: return cache[i]
            for word in wordDict:
                if len(s[i:]) < len(word): continue
                if s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        cache[i] = True
                        return cache[i]
            cache[i] = False
            return cache[i]
        return dfs(0)