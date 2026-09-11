class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area=0
        maxL = height[l]
        maxR = height[r]

        while(l<r):
            if(height[l] < height[r]):
                l+=1
                maxL = max(maxL, height[l])
                area += maxL-height[l]
            else:
                r-=1
                maxR = max(maxR, height[r])
                area += maxR-height[r]
        return area