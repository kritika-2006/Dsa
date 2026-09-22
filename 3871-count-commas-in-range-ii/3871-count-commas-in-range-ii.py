class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        p = 1000
        commas = 1
        
        while p <= n:
            next_p = p * 1000
            upper = min(n, next_p - 1)
            total += (upper - p + 1) * commas
            p = next_p
            commas += 1
            
        return total