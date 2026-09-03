class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)
        adj = {}
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                if pattern in adj: adj[pattern].append(word)
                else: adj[pattern] = [word]
        
        visit, q, res = set(), deque(), 1
        visit.add(beginWord)
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
        