class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = deque()
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasures.append((row, col, 0))

        def bfs(q):
            while q:
                r, c, dist = q.popleft()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647:
                        continue
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc, dist + 1))

        bfs(treasures)