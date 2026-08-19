class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap, visit, res, alreadyTaken = [[] for _ in range(numCourses)], set(), [], set()
        for crs, pre in prerequisites: preMap[crs].append(pre)
        def dfs(crs: int) -> bool:
            if crs in visit: return False # cycle
            if not preMap[crs]: # no prereq
                if crs not in alreadyTaken:
                    alreadyTaken.add(crs)
                    res.append(crs)
                return True 
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            res.append(crs)
            if crs not in alreadyTaken:
                alreadyTaken.add(crs)
                res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res
