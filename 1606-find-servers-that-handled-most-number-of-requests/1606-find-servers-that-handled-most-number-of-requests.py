import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  # Min-heap storing (free_time, server_id)
        available = SortedList(range(k))  # Sorted list of available server IDs
        request_count = [0] * k
        
        for i in range(len(arrival)):
            arr_time = arrival[i]
            dur = load[i]
            
            # Free up servers whose tasks have finished by arr_time
            while busy and busy[0][0] <= arr_time:
                _, s_id = heapq.heappop(busy)
                available.add(s_id)
                
            # If no servers are available, drop the request
            if not available:
                continue
                
            # Find the preferred server index starting from i % k
            start = i % k
            idx = available.bisect_left(start)
            
            # If no available server found >= start, wrap around to the first available server
            if idx == len(available):
                idx = 0
                
            s_id = available[idx]
            available.remove(s_id)
            
            # Assign task to server s_id
            request_count[s_id] += 1
            heapq.heappush(busy, (arr_time + dur, s_id))
            
        # Find the maximum number of requests handled by any server
        max_requests = max(request_count)
        
        # Return all servers that handled the maximum number of requests
        return [i for i, count in enumerate(request_count) if count == max_requests]

    # Aliases for platform compatibility
    busiestServers = busiestServers
    solve = busiestServers