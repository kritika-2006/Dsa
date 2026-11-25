class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Step 1: Build Suffix Array in O(N log N) via prefix doubling
        # Compress values to [0, n-1]
        unique_vals = sorted(set(nums))
        rank_map = {v: i for i, v in enumerate(unique_vals)}
        rank = [rank_map[v] for v in nums]
        sa = list(range(n))
        
        k = 1
        while k < n:
            # Sort suffixes based on pair (rank[i], rank[i + k])
            sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
            
            tmp = [0] * n
            for i in range(1, n):
                prev, curr = sa[i - 1], sa[i]
                prev_key = (rank[prev], rank[prev + k] if prev + k < n else -1)
                curr_key = (rank[curr], rank[curr + k] if curr + k < n else -1)
                tmp[curr] = tmp[prev] + (1 if curr_key != prev_key else 0)
            rank = tmp
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1

        # Step 2: Build LCP Array in O(N) using Kasai's algorithm
        # lcp[i] = LCP between sa[i] and sa[i + 1]
        lcp = [0] * (n - 1)
        h = 0
        for i in range(n):
            r = rank[i]
            if r < n - 1:
                j = sa[r + 1]
                while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                    h += 1
                lcp[r] = h
                if h > 0:
                    h -= 1

        # Step 3: Find minimum unique prefix length across all suffixes
        ans = n
        for i in range(n):
            left_lcp = lcp[i - 1] if i > 0 else 0
            right_lcp = lcp[i] if i < n - 1 else 0
            req_len = max(left_lcp, right_lcp) + 1
            
            # Must fit within the suffix starting at sa[i]
            if req_len <= n - sa[i]:
                if req_len < ans:
                    ans = req_len

        return ans

    # Aliases for platform method name compatibility
    minUniqueSubarray = smallestUniqueSubarray
    solve = smallestUniqueSubarray