class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, used = [], set()
        def dfs(path):
            if len(path) == len(nums): res.append(path.copy())
            for i in range(len(nums)):
                if nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                    dfs(path)
                    path.pop()
                    used.remove(nums[i])
        dfs([])
        return res