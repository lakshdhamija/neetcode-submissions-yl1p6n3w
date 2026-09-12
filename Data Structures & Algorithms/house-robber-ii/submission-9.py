class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)
        cache = {}
        def dfs(i, gold):
            if i >= len(gold): return 0
            if i in cache: return cache[i]
            robCurrentHouse = gold[i] + dfs(i + 2, gold)
            skipCurrentHouse = dfs(i + 1, gold)
            cache[i] = max(robCurrentHouse, skipCurrentHouse)
            return cache[i]
        firstHouseIncluded, lastHouseIncluded = nums[:len(nums) - 1], nums[1:]
        ans1 = dfs(0, firstHouseIncluded)
        cache = {}
        ans2 = dfs(0, lastHouseIncluded)
        return max(ans1, ans2)
