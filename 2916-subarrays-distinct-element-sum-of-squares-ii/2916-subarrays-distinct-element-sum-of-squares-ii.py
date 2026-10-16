class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree_sum = [0] * (4 * n)
        self.tree_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _apply(self, node, length, val):
        # (c + val)^2 = c^2 + 2*val*c + val^2 * length
        self.tree_sq[node] = (
            self.tree_sq[node] + 
            2 * val * self.tree_sum[node] + 
            val * val * length
        ) % self.MOD
        
        self.tree_sum[node] = (
            self.tree_sum[node] + 
            val * length
        ) % self.MOD
        
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self._apply(2 * node, mid - l + 1, self.lazy[node])
            self._apply(2 * node + 1, r - mid, self.lazy[node])
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self._apply(node, r - l + 1, val)
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
            
        self.tree_sum[node] = (self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]) % self.MOD
        self.tree_sq[node] = (self.tree_sq[2 * node] + self.tree_sq[2 * node + 1]) % self.MOD

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg = SegmentTree(n)
        
        last_occ = {}
        total_ans = 0
        current_sq_sum = 0
        
        for j in range(n):
            prev = last_occ.get(nums[j], -1)
            last_occ[nums[j]] = j
            
            # Update range [prev + 1, j] by adding +1 to distinct counts
            seg.update(1, 0, n - 1, prev + 1, j, 1)
            
            # The total sum of squares for all subarrays ending at index j 
            # is stored at the root of the segment tree (node 1 representing range [0, j])
            total_ans = (total_ans + seg.tree_sq[1]) % MOD
            
        return total_ans
        