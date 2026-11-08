class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Step 1: Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
                    
        communicating_servers = 0
        
        # Step 2: Check if each server can communicate
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_counts[i] > 1 or col_counts[j] > 1:
                        communicating_servers += 1
                        
        return communicating_servers

    # Aliases for platform method name compatibility
    countServers = countServers
    solve = countServers