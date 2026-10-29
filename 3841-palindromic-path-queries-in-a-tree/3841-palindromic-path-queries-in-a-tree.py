import sys

# Increase recursion depth for deep trees during HLD preprocessing
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, n, init_vals):
        self.n = n
        self.tree = [0] * (4 * n)
        self._build(1, 0, n - 1, init_vals)

    def _build(self, node, start, end, init_vals):
        if start == end:
            self.tree[node] = init_vals[start]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid, init_vals)
        self._build(2 * node + 1, mid + 1, end, init_vals)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 ^ p2

class Solution:
    def solve(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n
        
        # 1st DFS: compute subtree sizes, parent, depth, and heavy child
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            sz[u] = 1
            max_sz = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sz:
                        max_sz = sz[v]
                        heavy[u] = v

        dfs1(0, -1, 0)
        
        # 2nd DFS: compute heavy-light chain heads and positions
        cur_pos = 0
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)
        
        # Initialize Segment Tree with character masks
        init_vals = [0] * n
        s_list = list(s)
        for i in range(n):
            init_vals[pos[i]] = 1 << (ord(s_list[i]) - ord('a'))
            
        seg = SegmentTree(n, init_vals)
        
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= seg.query(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                ui = int(parts[1])
                c = parts[2]
                s_list[ui] = c
                seg.update(1, 0, n - 1, pos[ui], 1 << (ord(c) - ord('a')))
            else:
                ui = int(parts[1])
                vi = int(parts[2])
                mask = query_path(ui, vi)
                # A string can form a palindrome if at most one character has an odd count (mask has <= 1 set bit)
                if (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans

    # Aliases for method name compatibility
    palindromePath = solve
    canMakePalindromeQueries = solve
    solve = solve