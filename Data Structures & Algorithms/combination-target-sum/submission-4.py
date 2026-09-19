class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path, curSum = [], [], 0
        def dfs(i):
            nonlocal curSum
            if curSum == target:
                res.append(path.copy())
                return
            if i >= len(nums) or curSum > target: return
            curSum += nums[i]
            path.append(nums[i])
            dfs(i)
            path.pop()
            curSum -= nums[i]
            dfs(i + 1)
        dfs(0)
        return res