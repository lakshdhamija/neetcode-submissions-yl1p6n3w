class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            time = 0
            for pile in piles: time += math.ceil(pile / k)
            if time > h: # too slow
                l = k + 1
            else: # try to go faster
                r = k - 1
        return l
