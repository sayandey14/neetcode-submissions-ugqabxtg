class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i in range(len(heights)):
            area = heights[i]
            maxarea = max(maxarea, area)

            if not stack:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]

                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1

                    maxarea = max(maxarea, h * width)
                stack.append(i)
        
        n = len(heights)
        while stack:
            h = heights[stack.pop()]

            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1

            maxarea = max(maxarea, h * width)
            
        return maxarea
            