class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        def sq(x: int) -> int:
            sum1 = 0
            while(x>0):
                sum1 = sum1+((x%10)*(x%10))
                x//=10
            return sum1
        
        while(sq(n) not in seen):
            if(n==1):
                return True
            seen.append(n)
            n = sq(n)
        return False