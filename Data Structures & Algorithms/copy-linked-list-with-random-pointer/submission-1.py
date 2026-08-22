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
        randomMap, curr = {}, head
        while curr:
            newNode = Node(curr.val)
            randomMap[curr] = newNode
            curr = curr.next
        curr = head
        while curr:
            copyNode = randomMap[curr]
            if curr.next: copyNode.next = randomMap[curr.next]
            if curr.random: copyNode.random = randomMap[curr.random]
            curr = curr.next
        return randomMap[head]
