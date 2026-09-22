class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] stores the minimum length of a sub-array with sum = target ending at or before index i
        min_len = [float('inf')] * n
        prefix_sum_map = {0: -1}
        
        curr_sum = 0
        min_so_far = float('inf')
        ans = float('inf')
        
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum - target in prefix_sum_map:
                left = prefix_sum_map[curr_sum - target]
                length = i - left
                
                # If there is a valid non-overlapping sub-array to the left
                if left >= 0 and min_len[left] != float('inf'):
                    ans = min(ans, length + min_len[left])
                    
                min_so_far = min(min_so_far, length)
                
            min_len[i] = min_so_far
            prefix_sum_map[curr_sum] = i
            
        return ans if ans != float('inf') else -1