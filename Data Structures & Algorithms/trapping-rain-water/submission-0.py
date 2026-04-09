class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if not height:
            return 0

        l=0
        r=len(height)-1
        maxL = height[l]
        maxR = height[r]


        while(l<r):

            if(maxL<maxR):
                l+=1
                maxL = max(maxL, height[l])
                res += maxL-height[l] # wont be neg cuz previous line


            else:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR-height[r]
        
        return res
            