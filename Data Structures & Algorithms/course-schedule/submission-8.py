class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap, visit = [[] for _ in range(numCourses)], set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs: int) -> bool:
            if crs in visit: return False
            if not preMap[crs]: return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

