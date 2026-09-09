class PrefixTree:

    def __init__(self):
        self.isWord = False
        self.children = {}        

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children: cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]
        return True
        