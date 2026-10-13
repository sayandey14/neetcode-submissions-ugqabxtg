class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Base case: we matched every character in the word
            if i == len(word):
                return True
            
            # Check bounds, character match, and if already visited
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            path.add((r, c))
            
            # Explore all 4 neighboring directions
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # Backtrack
            path.remove((r, c))
            return res

        # Try starting the search from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    
        return False