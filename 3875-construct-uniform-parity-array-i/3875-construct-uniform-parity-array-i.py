from typing import List

class Solution:
    def uniformArray(self, nums: List[int]) -> bool:
        has_odd = any(x % 2 != 0 for x in nums)
        has_even = any(x % 2 == 0 for x in nums)
        
        # Agar saare elements pehle se even hain ya odd hain, toh True
        if not has_odd or not has_even:
            return True
            
        # Agar odd aur even dono hain, tab bhi odd element ka use karke uniform parity ban sakti hai
        return True