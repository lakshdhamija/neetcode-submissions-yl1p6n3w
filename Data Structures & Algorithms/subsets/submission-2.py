class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(i, curSet):
            if i == len(nums):
                res.append(curSet)
                return
            backtracking(i + 1, curSet)
            backtracking(i + 1, curSet + [nums[i]])
        backtracking(0, [])
        return res