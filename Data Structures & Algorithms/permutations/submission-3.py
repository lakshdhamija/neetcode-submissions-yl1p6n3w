class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, visited = [], set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    path.append(num)
                    dfs(path)
                    visited.remove(num)
                    path.pop()
        dfs([])
        return res