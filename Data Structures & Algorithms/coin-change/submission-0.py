class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            ret = float("infinity")

            for coin in coins:
                if amount - coin >= 0:
                    ret = min(ret, 1 + dfs(amount-coin))
            
            memo[amount] = ret
            return ret
        
        minCoins = dfs(amount)

        if minCoins == float("infinity"):
            return -1
        return minCoins

        
        
