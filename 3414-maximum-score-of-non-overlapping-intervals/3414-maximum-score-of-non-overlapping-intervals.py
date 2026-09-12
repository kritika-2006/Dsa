import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
            
        arr.sort(key=lambda x: (x[1], x[3]))
        ends = [x[1] for x in arr]
        
        prev_idx = []
        for i in range(n):
            l = arr[i][0]
            idx = bisect.bisect_left(ends, l)
            prev_idx.append(idx - 1)
            
        def better(a, b):
            if a[0] != b[0]:
                return a[0] > b[0]
            return a[1] < b[1]
            
        dp = [[(-1, []) for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, [])
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = arr[i - 1]
            p = prev_idx[i - 1]
            
            for j in range(5):
                best_val = dp[i - 1][j]
                
                if j > 0:
                    prev_dp_idx = p + 1
                    prev_weight, prev_list = dp[prev_dp_idx][j - 1]
                    if prev_weight != -1:
                        new_weight = prev_weight + w
                        new_list = sorted(prev_list + [orig_idx])
                        candidate = (new_weight, new_list)
                        if better(candidate, best_val):
                            best_val = candidate
                            
                if better(dp[i - 1][j], best_val):
                    best_val = dp[i - 1][j]
                    
                dp[i][j] = best_val
                
        ans_weight = -1
        ans_list = []
        for j in range(5):
            w_val, list_val = dp[n][j]
            if w_val > ans_weight:
                ans_weight = w_val
                ans_list = list_val
            elif w_val == ans_weight and w_val != -1:
                if list_val < ans_list:
                    ans_list = list_val
                    
        return ans_list