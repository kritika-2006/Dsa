from typing import List

class Solution:
    def uniformArray(self, nums: List[int]) -> bool:
        has_odd = any(x % 2 != 0 for x in nums)
        has_even = any(x % 2 == 0 for x in nums)
        
        # Agar saare elements pehle se same parity ke hain
        if not has_odd or not has_even:
            return True
            
        # Sabse chhota odd element dhundhein
        min_odd = min(x for x in nums if x % 2 != 0)
        
        # Agar koi bhi even number 'min_odd' se chhota hai, 
        # toh usme se min_odd घटाने पर negative value ya galat parity ban sakती है।
        for x in nums:
            if x % 2 == 0 and x <= min_odd:
                return False
                
        return True