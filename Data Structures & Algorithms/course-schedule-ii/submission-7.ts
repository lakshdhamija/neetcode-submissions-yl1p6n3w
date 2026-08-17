class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses: number, prerequisites: number[][]): number[] {
        const adj: number[][] = Array.from({ length: numCourses }, () => []);
        for (const [crs, pre] of prerequisites) adj[crs].push(pre);
        const visiting = new Set<number>();
        const res: number[] = [];
        const inResSet = new Set<number>();
        const dfs = (crs: number): boolean => {
            if (visiting.has(crs)) return false;
            if (adj[crs].length === 0) {
                if (!inResSet.has(crs)) {
                    inResSet.add(crs);
                    res.push(crs);
                }
                return true;
            }
            visiting.add(crs);
            for (const pre of adj[crs]) {
                if (!dfs(pre)) return false;
            }
            visiting.delete(crs);
            adj[crs] = [];
            if (!inResSet.has(crs)) {
                inResSet.add(crs);
                res.push(crs);
            }
            return true;
        }
        for (let crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) return [];
        }
        return res;
    }
}
