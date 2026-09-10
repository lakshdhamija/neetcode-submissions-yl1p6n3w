# Kahn
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs) # we create graph in reverse here. So cur course is prereq to these courses (pre -> [crs])
            indegree[crs] += 1 # this course has a prereq
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0: q.append(crs) # course has no prereqs so can be taken right away
        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]: 
                indegree[nei] -= 1
                if indegree[nei] == 0: q.append(nei) # all prereqs clear for this crs so it can be taken now
        if finish != numCourses: return []
        return output