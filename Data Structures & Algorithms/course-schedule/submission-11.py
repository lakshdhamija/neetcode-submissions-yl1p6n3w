class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, adj = [0] * numCourses, {}
        for crs, pre in prerequisites:
            indegree[crs] += 1
            if pre not in adj: adj[pre] = []
            adj[pre].append(crs)
        q= deque()
        for crs in range(numCourses):
            if indegree[crs] == 0: q.append(crs)
        finish = 0
        while q:
            crs = q.popleft()
            finish += 1
            if crs in adj:
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0: q.append(nei)
        return finish == numCourses