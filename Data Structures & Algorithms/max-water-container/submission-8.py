class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1

        maxarea = 0

        while(l<r):
            area = (r-l) * (min(heights[r],heights[l]))
            maxarea = max(area, maxarea)

            if(heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        
            print(heights[l], heights[r])
        return maxarea