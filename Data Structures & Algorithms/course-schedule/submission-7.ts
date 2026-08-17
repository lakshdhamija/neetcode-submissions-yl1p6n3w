class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const adj: number[][] = Array.from({ length: numCourses }, () => []);
        for (const [crs, pre] of prerequisites) adj[crs].push(pre);
        console.log(adj);
        const visiting = new Set<number>(); // track of courses being visited
        const dfs = (crs: number): boolean => {
            if (visiting.has(crs)) return false; // cycle
            if (adj[crs].length === 0) return true; // no pre
            visiting.add(crs);
            for (const pre of adj[crs]) {
                if (!dfs(pre)) return false;
            }
            visiting.delete(crs);
            adj[crs] = [];
            return true;
        }
        for (let crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) return false;
        }
        return true;
    }
}
