class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(i, curSet):
            if i == len(nums):
                res.append(curSet)
                return
            include, exclude = list(curSet), list(curSet)
            include.append(nums[i])
            backtracking(i + 1, exclude)
            backtracking(i + 1, include)
        backtracking(0, [])
        return res