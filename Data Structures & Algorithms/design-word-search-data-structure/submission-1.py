class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word):
        cur = self
        for c in word:
            if not c in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def searchWord(self, word):
        # print("word", word)
        cur = self
        for i, c in enumerate(word):
            if c == '.':
                nextWord = word[i+1:]
                for child in cur.children.values():
                    if child.searchWord(nextWord): return True
                return False
            else:
                # print(c, cur.children)
                if c not in cur.children: return False
                cur = cur.children[c]
        return cur.isWord
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.addWord(word)

    def search(self, word: str) -> bool:
        return self.root.searchWord(word)
