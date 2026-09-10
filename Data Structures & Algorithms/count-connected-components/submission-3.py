class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for n1, n2 in edges:
            if n1 in adj: adj[n1].append(n2)
            else: adj[n1] = [n2]
            if n2 in adj: adj[n2].append(n1)
            else: adj[n2] = [n1]
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            if node in adj:
                for nei in adj[node]: dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res