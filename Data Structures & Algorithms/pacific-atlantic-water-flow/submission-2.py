class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []

        rows, cols = len(heights), len(heights[0])
        pacific, atl = set(), set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))

            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atl)
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atl)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atl:
                    ret.append([row, col])
        return ret