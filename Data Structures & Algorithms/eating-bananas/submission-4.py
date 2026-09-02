class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        l, r = 1, maxSpeed
        while l <= r:
            k = (l + r) // 2 # try with this speed
            time = 0
            for pile in piles: time += math.ceil(pile / k)
            if time > h: l = k + 1 # too slow so we go faster
            else: r = k - 1 # go slower
        return l