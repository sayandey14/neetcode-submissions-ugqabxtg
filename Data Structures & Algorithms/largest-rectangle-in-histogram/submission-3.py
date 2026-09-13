class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Stores tuples: (index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop bars that are taller than the current height h
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index  # Current height can extend back to popped index
            stack.append((start, h))

        # Process remaining elements in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea