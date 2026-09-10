"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        nodeMap = {}
        def dfs(nde):
            if nde in nodeMap: return
            nodeMap[nde] = Node(nde.val)
            for nei in nde.neighbors: dfs(nei)
        dfs(node)

        for nde, newNode in nodeMap.items():
            for nei in nde.neighbors: newNode.neighbors.append(nodeMap[nei])
        return nodeMap[node]
        
