class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res = 0
        lmax = height[l]
        rmax = height[r]

        while(l<r):
            if(lmax>rmax):
                r-=1
                rmax = max(rmax, height[r])
                res += rmax-height[r]
            else:
                l+=1
                lmax = max(lmax, height[l])
                res+= lmax-height[l]
        
        return res
