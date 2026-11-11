class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = float('inf')
        
        # Try all possible counts of 'both' items from 0 up to max(need1, need2)
        # To optimize, we only need to check around the greedy choices or iterate smart,
        # but since constraints can be large (need1, need2 <= 10^9), we can check boundary values:
        # 1. Buy using only individual items
        # 2. Buy max(need1, need2) using both items
        # 3. Buy min(need1, need2) using both items and remaining using individual items
        
        candidates = [0, max(need1, need2), min(need1, need2)]
        
        for k in candidates:
            if k < 0:
                continue
            rem1 = max(0, need1 - k)
            rem2 = max(0, need2 - k)
            total_cost = k * costBoth + rem1 * cost1 + rem2 * cost2
            ans = min(ans, total_cost)
            
        # Also check if costBoth is very cheap or expensive, we can loop or use algebraic bounds.
        # Let's test a few more points around min(need1, need2) if needed, or implement binary search/ternary search.
        
        return ans

    # Aliases for platform method name compatibility
    minimumCostToAcquireRequiredItems = minimumCost
    solve = minimumCost