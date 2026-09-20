class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for n1, n2 in edges:
            if n1 not in adj: adj[n1] = []
            adj[n1].append(n2)
            if n2 not in adj: adj[n2] = []
            adj[n2].append(n1)
        visit, cycle, cycleStart = set(), set(), -1
        def dfs(node, prevNode):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei == prevNode: continue
                if dfs(nei, node): # cycle
                    if cycleStart != -1: cycle.add(node)
                    if node == cycleStart: cycleStart = -1
                    return True
            return False
        dfs(1, -1)
        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle: return [n1, n2]