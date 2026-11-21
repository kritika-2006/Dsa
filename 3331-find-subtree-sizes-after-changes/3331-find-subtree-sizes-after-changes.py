class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = [-1] * 26
        
        # Iterative DFS to find closest ancestor with the same character
        # Tuple format: (node, state) -> state 0 = enter, state 1 = exit
        stack = [(0, 0)]
        saved_prev = [-1] * n
        
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - ord('a')
            
            if state == 0:
                if last_seen[c] != -1:
                    new_parent[u] = last_seen[c]
                saved_prev[u] = last_seen[c]
                last_seen[c] = u
                
                stack.append((u, 1))
                for v in adj[u]:
                    stack.append((v, 0))
            else:
                last_seen[c] = saved_prev[u]
                
        # Build the modified tree
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Iterative post-order traversal to compute subtree sizes
        ans = [1] * n
        order = []
        dfs_stack = [0]
        while dfs_stack:
            u = dfs_stack.pop()
            order.append(u)
            for v in new_adj[u]:
                dfs_stack.append(v)
                
        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
                
        return ans

    # Alias for platform method name compatibility
    solve = findSubtreeSizes