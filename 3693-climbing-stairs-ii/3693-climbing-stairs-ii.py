class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        c = [0] + costs
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            # Jump from i - 1
            dp[i] = dp[i - 1] + c[i] + 1
            
            # Jump from i - 2
            if i >= 2:
                dp[i] = min(dp[i], dp[i - 2] + c[i] + 4)
                
            # Jump from i - 3
            if i >= 3:
                dp[i] = min(dp[i], dp[i - 3] + c[i] + 9)
                
        return dp[n]

    # Aliases for platform method name compatibility
    climbStairsII = climbStairs
    solve = climbStairs