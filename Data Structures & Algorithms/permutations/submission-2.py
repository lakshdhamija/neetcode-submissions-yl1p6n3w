class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        numSet, res = set(), []
        def dfs(path):
            if len(path) == len(nums): res.append(path.copy())
            for num in nums:
                if num not in numSet:
                    numSet.add(num)
                    path.append(num)
                    dfs(path)
                    numSet.remove(num)
                    path.pop()
        dfs([])
        return res