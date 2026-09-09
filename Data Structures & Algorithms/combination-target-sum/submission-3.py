class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curSum, arr):
            if i >= len(nums) or curSum > target: return
            if curSum == target:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            dfs(i, curSum + nums[i], arr)
            arr.pop()
            dfs(i + 1, curSum, arr)
        dfs(0, 0, [])
        return res