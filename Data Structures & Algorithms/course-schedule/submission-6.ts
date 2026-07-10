class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const preMap: Record<number, number[]> = {};
        for (const [crs, pre] of prerequisites) {
            if(!(crs in preMap)) preMap[crs] = [];
            preMap[crs].push(pre);
        }
        const visited: Set<number> = new Set();
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
        for (let crs = 0; crs <= numCourses; crs++) {
            if (!dfs(crs)) return false;
        }
        return true;
    }
}
