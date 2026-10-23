class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []

        rows, cols = len(heights), len(heights[0])
        
        def dfs(r, c):
            nonlocal pacific
            nonlocal atl
            if (r, c) in visited:
                return
            visited.add((r, c))
            if(r == 0 or c == 0):
                pacific = True
            if(r == rows-1 or c == cols-1):
                atl = True
            if atl and pacific:
                return
            
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                pacific = False
                atl = False
                visited = set()
                dfs(row, col)
                if pacific and atl:
                    ret.append([row, col])
        return ret