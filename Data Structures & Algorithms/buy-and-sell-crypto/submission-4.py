class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i, j = 0, 0, 1
        while i < len(prices) and j < len(prices):
            if prices[j] - prices[i] >= 0:
                profit = max(profit, prices[j] - prices[i])
                j += 1
            else:
                i = j
                j += 1
        return profit