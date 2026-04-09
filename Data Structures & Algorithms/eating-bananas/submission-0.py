class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ret = r


        while(l<=r):
            div = (l+r)//2

            time = 0

            for i in piles:
                time += math.ceil(float(i) / div)
            if time <= h:
                ret = div
                r = div - 1
            else:
                l = div + 1
        return ret;



