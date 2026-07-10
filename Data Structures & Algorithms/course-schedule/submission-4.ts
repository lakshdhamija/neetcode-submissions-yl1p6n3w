class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const preReqObj: Record<number, number[]> = {}; // course -> [prereqs]
        for (const [course, preReq] of prerequisites) {
            if (!(course in preReqObj)) preReqObj[course] = [];
            preReqObj[course].push(preReq);
        }
        const canResolve = new Set<number>();
        const detectCycle = (cr: number, visited: Set<number>): boolean => {
            if (visited.has(cr)) return true;
            if (canResolve.has(cr)) return false; // no need to check further since we already checked this number
            visited.add(cr);
            if (cr in preReqObj) {
                for(const preCr of preReqObj[cr]) {
                    const cycleDetected = detectCycle(preCr, visited);
                    if (cycleDetected) return true;
                }
            }
            canResolve.add(cr);
            visited.delete(cr);
            return false;
        };
        for (let cr = 0; cr < numCourses; cr++) {
            const visited = new Set<number>();
            const cycleDetected = detectCycle(cr, visited);
            if (cycleDetected) return false;
        }
        return true;
    }
}
