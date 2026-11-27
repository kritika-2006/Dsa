class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        # Handle potential (budget, items) argument order discrepancy
        if isinstance(items, int):
            items, budget = budget, items
            
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
            
        # Precompute number of multiples (including self) for each factor
        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                total = 0
                for mult in range(f, max_f + 1, f):
                    total += freq[mult]
                multiples_count[f] = total
                
        # 0/1 Knapsack for the first copy of each item
        # dp[c] = max items gained using exact cost c (buying at most 1 of each item)
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = float('inf')
        
        for f, p in items:
            if p < min_price:
                min_price = p
            if p <= budget:
                gain = multiples_count[f]  # 1 purchased + (multiples_count[f] - 1) free
                for c in range(budget, p - 1, -1):
                    if dp[c - p] != -1 and dp[c - p] + gain > dp[c]:
                        dp[c] = dp[c - p] + gain
                        
        # Combine with unlimited copies of the cheapest item for any remaining budget
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra = (budget - c) // min_price
                if dp[c] + extra > ans:
                    ans = dp[c] + extra
                    
        return ans

    # Aliases for platform method name compatibility
    maxItems = maximumSaleItems
    maxNumberOfItems = maximumSaleItems
    maximumItems = maximumSaleItems
    solve = maximumSaleItems