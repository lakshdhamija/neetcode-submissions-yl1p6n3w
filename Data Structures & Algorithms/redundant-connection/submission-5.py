class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for n1, n2 in edges:
            if n1 in adj: adj[n1].append(n2)
            else: adj[n1] = [n2]
            if n2 in adj: adj[n2].append(n1)
            else: adj[n2] = [n1]
        cycleStart, visit, cycle = -1, set(), set()
        def dfs(node, prevNode):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            visit.add(node)
            if node in adj:
                for nei in adj[node]:
                    if nei == prevNode: continue
                    if dfs(nei, node):
                        if cycleStart != -1: cycle.add(node)
                        if cycleStart == node: cycleStart = -1
                        return True
            return False
        dfs(1, -1)
        for n1, n2 in edges[::-1]:
            if n1 in cycle and n2 in cycle: return [n1, n2]
        return []