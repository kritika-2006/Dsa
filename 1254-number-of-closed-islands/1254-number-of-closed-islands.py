class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == 1:
                return
            # Mark current land as visited by turning it into water (1)
            grid[r][c] = 1
            
            # Explore 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Flood fill (sink) all 0s connected to the borders
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs(r, c)
        
        # Step 2: Count remaining closed islands
        closed_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    closed_count += 1
                    dfs(r, c)
                    
        return closed_count

    # Aliases for safety
    numberOfClosedIslands = closedIsland