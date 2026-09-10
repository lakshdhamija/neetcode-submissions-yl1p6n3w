class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        adj = {}
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                if pattern not in adj: adj[pattern] = []
                adj[pattern].append(word)
        visit, q, res = set(), deque([beginWord]), 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1 # go to next hop
        return 0