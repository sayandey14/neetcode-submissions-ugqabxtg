class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        maxprofit = 0
        while(r<len(prices)):
            if(prices[r] < prices[l]):
                l = r
            maxprofit = max(maxprofit, prices[r] - prices[l])
            r+=1
        
        return maxprofit