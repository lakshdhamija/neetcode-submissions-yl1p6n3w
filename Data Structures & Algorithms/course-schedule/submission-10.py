class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, adj, q, finish = [0] * numCourses, {}, deque(), 0
        for crs, pre in prerequisites:
            indegree[crs] += 1 # course has prereq
            if pre in adj: adj[pre].append(crs)
            else: adj[pre] = [crs] # course -> key is the prereq course, val is the courses it is prereq to
        for crs in range(numCourses):
            if indegree[crs] == 0: q.append(crs)
        while q:
            pre = q.popleft()
            finish += 1
            if pre in adj:
                for crs in adj[pre]:
                    indegree[crs] -= 1
                    if indegree[crs] == 0: q.append(crs)
        return finish == numCourses
            
