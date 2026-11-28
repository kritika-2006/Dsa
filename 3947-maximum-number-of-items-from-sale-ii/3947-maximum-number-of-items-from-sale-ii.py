class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        # Handle potential (budget, items) argument order discrepancy
        if isinstance(items, int):
            items, budget = budget, items
            
        n = len(items)
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        min_price = float('inf')
        
        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p
                
        # Harmonic sieve to count multiples for each factor in O(N log N)
        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                total = 0
                for mult in range(f, max_f + 1, f):
                    total += freq[mult]
                multiples_count[f] = total
                
        # Sort items by price ascending to greedily buy cheapest 2-for-1 units
        items_sorted = sorted(items, key=lambda x: x[1])
        
        ans = 0
        rem_budget = budget
        limit_price = 2 * min_price
        
        for f, p in items_sorted:
            if p > limit_price or rem_budget < p:
                break
            cap = multiples_count[f] - 1
            if cap > 0:
                take = min(cap, rem_budget // p)
                ans += 2 * take
                rem_budget -= take * p
                
        # Spend any remaining budget on 1-copy units of the cheapest item
        ans += rem_budget // min_price
        return ans

    # Aliases for platform method name compatibility
    maxItems = maximumSaleItems
    maxNumberOfItems = maximumSaleItems
    maximumItems = maximumSaleItems
    solve = maximumSaleItems