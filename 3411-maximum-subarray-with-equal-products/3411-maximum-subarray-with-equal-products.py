import math

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 2  # Any pair of 2 positive integers satisfies a*b == lcm(a,b)*gcd(a,b)
        
        for i in range(n):
            curr_prod = 1
            curr_gcd = 0
            curr_lcm = 1
            
            for j in range(i, n):
                val = nums[j]
                curr_prod *= val
                curr_gcd = math.gcd(curr_gcd, val)
                curr_lcm = math.lcm(curr_lcm, val)
                
                if curr_prod == curr_lcm * curr_gcd:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                elif curr_prod > 25200:
                    # Max possible lcm(1..10) * max_gcd(10) = 2520 * 10 = 25200
                    break
                    
        return max_len

    # Alias for platform method name compatibility
    solve = maxLength