class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        zero, one = 0, 0
        for i in range(2, len(cost) + 1):
            two = min(one + cost[i - 1], zero + cost[i - 2]) # we can come to 2 from prev step or 0th step
            one, zero = two, one
        return one