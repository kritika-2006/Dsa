class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # dp[i][j] stores the number of ways to reach cell (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                
                ways = dp[i][j]
                
                # 1. Try moving RIGHT from (i, j)
                if j + 1 < n:
                    ni, nj = i, j + 1
                    # Handle continuous reflections if we hit mirror cells
                    valid = True
                    # Direction we are entering the cell: 'R' (moving right) or 'D' (moving down)
                    dir_moving = 'R' 
                    
                    while ni < m and nj < n and grid[ni][nj] == 1:
                        if dir_moving == 'R':
                            # Turning down
                            ni += 1
                            dir_moving = 'D'
                        else:
                            # Turning right
                            nj += 1
                            dir_moving = 'R'
                    
                    # Check if the final landing cell is within bounds and valid
                    if ni < m and nj < n:
                        dp[ni][nj] = (dp[ni][nj] + ways) % MOD
                
                # 2. Try moving DOWN from (i, j)
                if i + 1 < m:
                    ni, nj = i + 1, j
                    valid = True
                    dir_moving = 'D'
                    
                    while ni < m and nj < n and grid[ni][nj] == 1:
                        if dir_moving == 'R':
                            ni += 1
                            dir_moving = 'D'
                        else:
                            nj += 1
                            dir_moving = 'R'
                            
                    if ni < m and nj < n:
                        dp[ni][nj] = (dp[ni][nj] + ways) % MOD
                        
        return dp[m - 1][n - 1]

    # Aliases for platform method name compatibility
    twistedMirrorPathCount = uniquePaths
    solve = uniquePaths