class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.start, self.end = Node(0, 0), Node(0, 0)
        self.start.next, self.end.prev = self.end, self.start

    def addNode(self, node: Node):
        prev, nxt = self.end.prev, self.end
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def removeNode(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.removeNode(self.cache[key])
        node = Node(key, value)
        self.addNode(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.start.next
            self.removeNode(lru)
            del self.cache[lru.key]
