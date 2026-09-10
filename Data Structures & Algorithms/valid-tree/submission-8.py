class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for node1, node2 in edges:
            if node1 in adj: adj[node1].append(node2)
            else: adj[node1] = [node2]
            if node2 in adj: adj[node2].append(node1)
            else: adj[node2] = [node1]
        visited = set()
        # print(adj)
        def dfs(node, parent):
            # print(node, cycle)
            if node in visited: return False
            visited.add(node)
            if node in adj:
                for nei in adj[node]:
                    if nei == parent: continue
                    if not dfs(nei, node): return False
            return True
        if not dfs(0, -1): return False
        if len(visited) != n: return False
        return True