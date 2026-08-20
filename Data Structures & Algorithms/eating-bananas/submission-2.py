class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        l, r, res = 1, maxSpeed, float('inf')
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles: time += math.ceil(pile / mid)
            if time > h: l = mid + 1 # not able to complete food, go faster
            else: # we were able to complete the piles so we try and go slower
                res = min(res, mid)
                r = mid - 1
        return res