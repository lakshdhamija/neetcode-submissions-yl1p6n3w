class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, res, cycle, alreadyTaken = {}, [], set(), set()
        for crs, pre in prerequisites:
            if crs in adj: adj[crs].append(pre)
            else: adj[crs] = [pre]
        def dfs(crs):
            if crs in cycle: return False
            if crs in alreadyTaken: return True
            cycle.add(crs)
            if crs in adj:
                for pre in adj[crs]:
                    if not dfs(pre): return False
            res.append(crs)
            alreadyTaken.add(crs)
            adj[crs] = []
            cycle.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res
        