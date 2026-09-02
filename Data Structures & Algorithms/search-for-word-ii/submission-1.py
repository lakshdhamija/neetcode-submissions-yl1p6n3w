class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def getWord(self, word): # not needed - just for fun
        cur = self
        for c in word:
            if c not in word: return False
            cur = cur.children[c]
        cur.isWord = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words: root.addWord(word)
        ROWS, COLS, dirs = len(board), len(board[0]), [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] not in node.children: return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord: res.add(word)
            for dr, dc in dirs: dfs(r + dr, c + dc, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)


















