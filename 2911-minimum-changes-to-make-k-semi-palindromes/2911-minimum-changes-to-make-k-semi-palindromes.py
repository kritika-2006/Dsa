class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # 1. Precompute proper divisors for all lengths from 2 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # 2. Precompute minimum changes to make s[i..j] a semi-palindrome
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = INF
                
                for d in divisors[length]:
                    changes = 0
                    group_len = length // d
                    for rem in range(d):
                        left = i + rem
                        right = left + (group_len - 1) * d
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                        
                cost[i][j] = min_changes
                
        # 3. DP to partition s[0..j] into p semi-palindromes
        dp = [[INF] * n for _ in range(k + 1)]
        
        for j in range(1, n):
            dp[1][j] = cost[0][j]
            
        for p in range(2, k + 1):
            # Minimum index j needed to form p substrings of length >= 2 is 2*p - 1
            for j in range(2 * p - 1, n):
                for i in range(2 * (p - 1), j):
                    if dp[p - 1][i - 1] + cost[i][j] < dp[p][j]:
                        dp[p][j] = dp[p - 1][i - 1] + cost[i][j]
                        
        return dp[k][n - 1]

    solve = minimumChanges