class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtracking(i, curSet):
            if i == len(nums):
                res.append(curSet[:])
                return
            curSet.append(nums[i])
            backtracking(i + 1, curSet)
            curSet.pop()
            backtracking(i + 1, curSet)
        backtracking(0, [])
        return res