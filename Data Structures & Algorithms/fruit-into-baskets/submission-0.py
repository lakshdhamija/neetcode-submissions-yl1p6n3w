class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsMap, res, l, r = {}, 0, 0, 0
        while r < len(fruits):
            fruitsMap[fruits[r]] = fruitsMap.get(fruits[r], 0) + 1
            while len(fruitsMap) > 2: # not valid
                fruitsMap[fruits[l]] -= 1
                if not fruitsMap[fruits[l]]: del fruitsMap[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res