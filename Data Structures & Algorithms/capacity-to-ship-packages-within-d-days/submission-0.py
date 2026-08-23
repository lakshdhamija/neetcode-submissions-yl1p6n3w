class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r, res = max(weights), sum(weights), 0
        while l <= r:
            mid = (l + r) // 2
            # calculate number of days it will take to load everything with daily capacity as mid
            weightRemaining, daysTaken = mid, 1
            for weight in weights:
                if weight <= weightRemaining: weightRemaining -= weight
                else:
                    weightRemaining = mid - weight
                    daysTaken += 1
            if daysTaken <= days:
                r = mid - 1 # we try loading less cause we're in limit
                res = mid
            else: l = mid + 1 # need to go faster as we're consuming more days
        return res
        
