class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        for i in range(0,len(prices)):
            cur = prices[i]
            for j in range(i,len(prices)):
                if(prices[j]-prices[i]>max1):
                    max1 = prices[j]-prices[i]
        return max1