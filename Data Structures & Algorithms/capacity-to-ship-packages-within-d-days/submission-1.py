class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r, res = max(weights), sum(weights), 0
        while l <= r:
            mid = (l + r) // 2
            daysTaken, i, cap = 0, 0, mid
            while i < len(weights):
                daysTaken += 1
                while i < len(weights) and weights[i] <= cap:
                    cap -= weights[i]
                    i += 1
                cap = mid
            if daysTaken <= days:
                res = mid
                r = mid - 1
            else: l = mid + 1
        return res