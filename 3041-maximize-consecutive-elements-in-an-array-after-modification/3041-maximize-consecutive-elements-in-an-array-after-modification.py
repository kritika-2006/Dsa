class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0
        
        for x in nums:
            # Update x + 1 first so we don't reuse the current element x twice
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
            
            ans = max(ans, dp[x], dp[x + 1])
            
        return ans

    # Alias for platform method name compatibility
    solve = maxSelectedElements