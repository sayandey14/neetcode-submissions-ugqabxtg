class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        visited = set()

        queue = deque()

        def add(r, c):
            if(r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c] == -1):
                return
            
            visited.add((r,c))
            queue.append([r,c])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row,col])
                    visited.add((row,col))
        

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft() #all the treasure(0) will always have a dist of 0 and its alr in visited so the bfs will never visit it, and it will never visit land cuz bfs dont visit land either
                grid[r][c] = dist
                add(r+1, c)
                add(r-1, c)
                add(r, c+1)
                add(r, c-1)
            dist+=1
        

