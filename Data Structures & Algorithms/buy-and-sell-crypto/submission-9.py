class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minBuy = prices[0]

        for cur in prices:
            max_profit = max(max_profit, cur - minBuy)
            minBuy = min(minBuy, cur)
        
        return max_profit