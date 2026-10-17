class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        def rot(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            fresh -= 1
            queue.append((r, c))

        if fresh == 0:
            return 0

        tick = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            tick += 1
            if fresh == 0:
                return tick

        return -1