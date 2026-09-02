class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            backtracking(i + 1, path)
            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()
        backtracking(0, [])
        return res