class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # last dictionary keeps track of the last seen index/count contribution of each character
        last = {}
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Empty subsequence
        
        for i, char in enumerate(s):
            # Total distinct subsequences so far can be doubled
            dp[i + 1] = (dp[i] * 2) % MOD
            
            # If the character has appeared before, subtract the subsequences 
            # that were already counted when that character last appeared
            if char in last:
                dp[i + 1] = (dp[i + 1] - dp[last[char]]) % MOD
                
            last[char] = i
            
        # Subtract 1 to exclude the empty subsequence, and handle negative modulo
        return (dp[len(s)] - 1 + MOD) % MOD