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
        visit, q, res = set(), deque(), 1
        visit.add(beginWord)
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

