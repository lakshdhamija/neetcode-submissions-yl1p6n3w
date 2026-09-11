class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for word in words for c in word }
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if word1[:minLen] == word2[:minLen] and len(word1) > minLen: return ""
            j = 0
            while j < minLen:
                if word1[j] == word2[j]: j += 1
                else:
                    adj[word1[j]].add(word2[j])
                    break
        visit, cycle, res = set(), set(), []
        def dfs(c):
            if c in cycle: return True # cycle detected, invalid
            if c in visit: return False # no cycle but c is already in the output
            cycle.add(c)
            visit.add(c)
            for nei in adj[c]:
                if dfs(nei): return True
            cycle.remove(c)
            res.append(c)
            return False
        for c in adj:
            if dfs(c): return ""
        return "".join(res[::-1])