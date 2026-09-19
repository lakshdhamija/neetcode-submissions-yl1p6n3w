class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curSum = [], 0
        candidates.sort()
        def dfs(i, path):
            nonlocal curSum
            if curSum == target:
                res.append(path.copy())
                return
            if curSum > target or i >= len(candidates): return
            curSum += candidates[i]
            path.append(candidates[i])
            dfs(i + 1, path)
            curSum -= candidates[i]
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: i += 1
            dfs(i + 1, path)
        dfs(0, [])
        return res
            