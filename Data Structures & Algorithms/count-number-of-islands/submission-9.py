class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0            
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0
        def dfs(r, c):
            # Base case: stop if out of bounds, already visited, or hits water/invalid state
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                grid[r][c] == "0" or  # (adjust condition based on the specific problem)
                (r, c) in visited):
                return
            # Mark current position as visited
            visited.add((r, c))
            # Explore all 4 directions to link the component together
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        # 1. Loop through every single cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # 2. If it's an unvisited target node, it's a new component!
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)  # 3. DFS links and marks the whole component
        return count