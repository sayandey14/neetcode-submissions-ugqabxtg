class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ret = 0
        while (l <= r):
            mid = (l+r)//2
            time = 0

            for i in piles:
                time += ((i+mid-1)//mid)
            
            if time > h:
                l = mid + 1
            else:
                if(ret == 0):
                    ret = mid
                else:
                    ret = min(ret, mid)
                r = mid - 1
        
        return ret
