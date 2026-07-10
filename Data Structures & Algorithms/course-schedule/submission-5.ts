class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const preMap: Record<number, number[]> = {};
        for (const [cr, pre] of prerequisites) {
            if (!(cr in preMap)) preMap[cr] = [];
            preMap[cr].push(pre);
        }
        const visited = new Set<number>(); // nodes along the current dfs path
        const dfs = (crs: number): boolean => {
            if (visited.has(crs)) return false;
            if (!(crs in preMap) || preMap[crs].length === 0) return true;
            visited.add(crs);
            for (const pre of preMap[crs]) {
                if (!dfs(pre)) return false;
            }
            visited.delete(crs);
            preMap[crs] = [];
            return true;
        }
        for (let crs = 0; crs < numCourses; crs++) {
            if (!dfs(crs)) return false;
        }
        return true;
    }
}
