class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, res = 0, 0, 0
        while r < len(prices):
            if prices[r] < prices[l]: l = r
            else: res = max(res, prices[r] - prices[l])
            r += 1
        return res