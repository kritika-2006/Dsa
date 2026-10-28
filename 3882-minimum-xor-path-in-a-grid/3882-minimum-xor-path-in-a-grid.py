class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[r][c] stores a set of all possible XOR path values to cell (r, c)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                current_val = grid[r][c]
                prev_vals = set()
                
                if r > 0:
                    prev_vals.update(dp[r - 1][c])
                if c > 0:
                    prev_vals.update(dp[r][c - 1])
                
                for v in prev_vals:
                    dp[r][c].add(v ^ current_val)
                    
        return min(dp[m - 1][n - 1])

    # Aliases for platform method name mismatches
    minXorPath = minCost
    minCostPath = minCost
    solve = minCost