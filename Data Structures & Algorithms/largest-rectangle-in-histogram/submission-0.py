class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxarea = max(maxarea, height * (i-idx))
                start = idx

            stack.append([start, h])

        for i, h in stack:
            maxarea = max(maxarea, h*(len(heights) - i))
        
        return maxarea
