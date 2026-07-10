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
        const cycle: Set<number> = new Set(), visit: Set<number> = new Set(), output: number[] = [];
        const dfs = (crs: number): boolean => {
            if (cycle.has(crs)) return false; // cycle detected
            if (visit.has(crs)) return true; // already in output
            cycle.add(crs);
            if (crs in preMap) {
                for (const pre of preMap[crs]) {
                    if (!dfs(pre)) return false;
                }
            }
            visit.add(crs);
            cycle.delete(crs);
            output.push(crs);
            return true;
        }

        for (let crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) return [];
        }
        return output;
    }
}
