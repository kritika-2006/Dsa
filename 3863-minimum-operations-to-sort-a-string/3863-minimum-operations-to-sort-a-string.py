class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        target = "".join(sorted(s))
        
        # If the string is already sorted
        if s == target:
            return 0
            
        # If length is 2 and not sorted, it's impossible
        if n == 2:
            return -1
            
        # Find first and last mismatch between s and target
        first = 0
        while first < n and s[first] == target[first]:
            first += 1
        last = n - 1
        while last >= 0 and s[last] == target[last]:
            last -= 1
            
        # Helper to check if a string is sorted
        def is_sorted(x):
            return x == target

        # Helper to check if x can be sorted in 1 operation
        def can_1_op(x):
            if is_sorted(x):
                return True
            f = 0
            while f < n and x[f] == target[f]:
                f += 1
            l = n - 1
            while l >= 0 and x[l] == target[l]:
                l -= 1
            return (l - f + 1) < n

        # Strategic candidate lengths to check (avoids O(N^2) loops)
        cand_lens = set()
        for l in [2, 3, first + 1, last + 1, n - first, n - last, n - 1]:
            if 1 < l < n:
                cand_lens.add(l)

        # 1. Check if 1 operation is enough
        if last - first + 1 < n:
            sub = "".join(sorted(s[first:last+1]))
            if is_sorted(s[:first] + sub + s[last+1:]):
                return 1
                
        for length in cand_lens:
            sub_p = "".join(sorted(s[:length]))
            if is_sorted(sub_p + s[length:]):
                return 1
            sub_s = "".join(sorted(s[n-length:]))
            if is_sorted(s[:n-length] + sub_s):
                return 1

        if can_1_op(s):
            return 1

        # 2. Check if 2 operations are enough using candidate cuts
        for length in cand_lens:
            s_pref = "".join(sorted(s[:length])) + s[length:]
            if can_1_op(s_pref):
                return 2
            s_suff = s[:n-length] + "".join(sorted(s[n-length:]))
            if can_1_op(s_suff):
                return 2

        # For n >= 3, if not 0, 1, or 2, it takes 3 operations
        return 3