class Solution:
    def firstStableIndex(self, arr: list[int], threshold: int) -> int:
        n = len(arr)
        
        # Precompute or check running conditions for stability
        # Typically, a stable index requires running maximums/minimums or prefix sums.
        # Here is the general efficient O(N) structure for stable index problems:
        
        left_max = [0] * n
        right_min = [0] * n
        
        cur_max = -float('inf')
        for i in range(n):
            cur_max = max(cur_max, arr[i])
            left_max[i] = cur_max
            
        cur_min = float('inf')
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, arr[i])
            right_min[i] = cur_min
            
        for i in range(n):
            # Check stability condition based on threshold or prefix/suffix logic
            if left_max[i] - right_min[i] <= threshold:
                return i
                
        return -1