class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, arr, curSum):
            if curSum == target:
                res.append(arr.copy())
                return
            if i >= len(candidates) or curSum > target: return
            arr.append(candidates[i])
            dfs(i + 1, arr, curSum + candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: i += 1
            dfs(i + 1, arr, curSum)
        dfs(0, [], 0)
        return res