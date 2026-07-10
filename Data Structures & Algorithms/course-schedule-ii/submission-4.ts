class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses: number, prerequisites: number[][]): number[] {
        const preMap: Record<number, number[]> = {};
        for (const [crs, pre] of prerequisites) {
            if (!(crs in preMap)) preMap[crs] = [];
            preMap[crs].push(pre);
        }
        const output: number[] = [];
        const visited: Set<number> = new Set(), cycle: Set<number> = new Set();
        const dfs = (crs: number): boolean => {
            if (cycle.has(crs)) return false; // cycle detected
            if (visited.has(crs)) return true; // already visited
            cycle.add(crs);
            if(crs in preMap) {
                for (const pre of preMap[crs]) {
                    if (!dfs(pre)) return false;
                }
            }
            cycle.delete(crs);
            visited.add(crs);
            output.push(crs);
            return true;
        }
        for (let crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) return [];
        }
        return output;
    }
}
