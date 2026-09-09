class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visit = [], set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.add(nums[i])
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    visit.remove(nums[i])
        dfs([])
        return res