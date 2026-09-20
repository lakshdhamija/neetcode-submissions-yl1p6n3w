class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for crs, pre in prerequisites:
            if crs not in adj: adj[crs] = []
            adj[crs].append(pre)
        res, cycle, visit = [], set(), set()
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            cycle.add(crs)
            visit.add(crs)
            if crs in adj:
                for pre in adj[crs]:
                    if not dfs(pre): return False
            res.append(crs)
            cycle.remove(crs)
            adj[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res