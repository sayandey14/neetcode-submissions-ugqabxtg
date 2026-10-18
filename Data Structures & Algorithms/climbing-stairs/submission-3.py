class Solution:
    def climbStairs(self, n: int) -> int:
        #memoization
        hashmap = {}
        def dfs(n):
            result = 0
            if n in hashmap:
                return hashmap[n]
            if n == 1:
                result = 1
            elif n == 2:
                result = 2
            else:
                result = dfs(n-1)+dfs(n-2)
                hashmap[n] = result
            return result
        
        return dfs(n)