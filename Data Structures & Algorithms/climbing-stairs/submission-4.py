class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up sol
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        array = [0]*(n+1)
        array[1] = 1
        array[2] = 2

        for i in range(3,n+1):
            array[i] = array[i-1] + array[i-2]
        
        return array[n]