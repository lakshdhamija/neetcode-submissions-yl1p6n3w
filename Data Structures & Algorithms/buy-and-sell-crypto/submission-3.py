class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, l, r = 0, 0, 1
        while l < r and l < len(prices) and r < len(prices):
            buy = prices[l]
            sell = prices[r]
            print(l, r, buy, sell)
            if sell - buy < 0: l = r
            profit = max(profit, sell - buy)
            r += 1
        return profit

