class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        # Helper function to find all palindrome substrings of length >= k
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                l -= 1
                r += 1

        # Check all possible centers for odd and even length palindromes
        for i in range(n):
            expand(i, i)     # Odd length
            expand(i, i + 1) # Even length
            
        # Greedy interval scheduling: sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r
                
        return count