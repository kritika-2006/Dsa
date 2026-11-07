import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        
        # Free servers heap: stores tuples of (weight, index)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        # Busy servers heap: stores tuples of (free_time, weight, index)
        busy_servers = []
        
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            # Advance current time to at least j if no servers are free and current_time < j
            current_time = max(current_time, j)
            
            # If no free servers available, jump time to when the next server becomes free
            if not free_servers and busy_servers:
                current_time = max(current_time, busy_servers[0][0])
                
            # Move all servers that have finished their tasks by current_time back to free_servers
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            # Assign the task to the best available free server
            weight, idx = heapq.heappop(free_servers)
            ans[j] = idx
            
            # Push the server into busy_servers with its new free time
            finish_time = current_time + tasks[j]
            heapq.heappush(busy_servers, (finish_time, weight, idx))
            
        return ans

    # Aliases for platform method name compatibility
    solve = assignTasks