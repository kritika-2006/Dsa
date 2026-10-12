class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        bit_counts = [0] * 32
        for x in nums:
            for bit in range(32):
                if (x & (1 << bit)):
                    bit_counts[bit] += 1
                    
        # Reconstruct numbers by placing bits greedily
        res_nums = [0] * len(nums)
        for bit in range(32):
            count = bit_counts[bit]
            for i in range(count):
                res_nums[i] |= (1 << bit)
                
        # Sort descending to pick the top k largest numbers
        res_nums.sort(reverse=True)
        
        ans = 0
        MOD = 10**9 + 7
        for i in range(k):
            ans = (ans + res_nums[i] * res_nums[i]) % MOD
            
        return ans