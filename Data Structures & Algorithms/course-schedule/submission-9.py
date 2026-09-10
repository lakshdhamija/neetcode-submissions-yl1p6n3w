class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for crs, pre in prerequisites:
            if crs not in adj: adj[crs] = [pre]
            else: adj[crs].append(pre)
        visited = set()
        def dfs(crs):
            if crs in visited: return False
            visited.add(crs)
            if crs in adj:
                for pre in adj[crs]:
                    if not dfs(pre): return False
            visited.remove(crs)
            adj[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True