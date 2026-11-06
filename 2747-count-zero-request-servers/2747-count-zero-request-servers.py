class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while preserving their original indices
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        
        ans = [0] * len(queries)
        active_servers = {}
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q, orig_idx in sorted_queries:
            window_start = q - x
            window_end = q
            
            # Expand right pointer to include logs up to window_end
            while right < num_logs and logs[right][1] <= window_end:
                srv = logs[right][0]
                active_servers[srv] = active_servers.get(srv, 0) + 1
                right += 1
                
            # Shrink left pointer to exclude logs before window_start
            while left < num_logs and logs[left][1] < window_start:
                srv = logs[left][0]
                active_servers[srv] -= 1
                if active_servers[srv] == 0:
                    del active_servers[srv]
                left += 1
                
            # Total servers - servers that received at least one request
            ans[orig_idx] = n - len(active_servers)
            
        return ans

    # Aliases for platform method name compatibility
    countZeroRequestServers = countServers
    solve = countServers