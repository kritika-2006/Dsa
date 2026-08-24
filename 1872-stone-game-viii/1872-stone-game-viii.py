class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Calculate prefix sums
        pref = stones[:]
        for i in range(1, n):
            pref[i] += pref[i - 1]
            
        # Base case: if we take all stones up to the last index (n-1)
        # The score difference is simply pref[n-1] because no turns remain.
        dp = pref[-1]
        
        # Iterate backwards from index n - 2 down to 1
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp