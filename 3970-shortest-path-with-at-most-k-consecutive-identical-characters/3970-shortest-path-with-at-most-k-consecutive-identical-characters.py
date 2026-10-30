import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        start_char = ord(labels[0]) - ord('a')
        
        # Priority queue stores: (weight, u, char_idx, streak)
        pq = [(0, 0, start_char, 1)]
        dist = {(0, start_char, 1): 0}
        
        while pq:
            d, u, char_idx, streak = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > dist.get((u, char_idx, streak), float('inf')):
                continue
                
            for v, w in adj[u]:
                next_char = ord(labels[v]) - ord('a')
                if next_char == char_idx:
                    new_streak = streak + 1
                else:
                    new_streak = 1
                    
                if new_streak > k:
                    continue
                    
                nd = d + w
                state = (v, next_char, new_streak)
                if nd < dist.get(state, float('inf')):
                    dist[state] = nd
                    heapq.heappush(pq, (nd, v, next_char, new_streak))
                    
        return -1

    # Aliases for platform method name mismatches
    shortestPath = minCost
    minPath = minCost
    solve = minCost