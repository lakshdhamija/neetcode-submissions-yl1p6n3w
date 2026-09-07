"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        nodesMap, curr = {}, head
        while curr:
            newNode = Node(curr.val)
            nodesMap[curr] = newNode
            curr = curr.next
        curr = head
        while curr:
            mappedNode = nodesMap[curr]
            nxtMappedNode = nodesMap[curr.next] if curr.next else None
            randomMappedNode = nodesMap[curr.random] if curr.random else None
            mappedNode.next = nxtMappedNode
            mappedNode.random = randomMappedNode
            curr = curr.next
        return nodesMap[head]