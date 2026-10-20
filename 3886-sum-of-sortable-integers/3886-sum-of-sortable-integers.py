class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        total_sum = 0
        
        for k in range(1, n + 1):
            if n % k == 0:
                valid = True
                for i in range(0, n, k):
                    chunk = nums[i:i+k]
                    sorted_chunk = sorted_nums[i:i+k]
                    
                    # Fast O(k) check for cyclic shift against a sorted array
                    k_len = len(chunk)
                    drops = 0
                    drop_idx = -1
                    
                    for j in range(k_len):
                        if chunk[j] > chunk[(j + 1) % k_len]:
                            drops += 1
                            drop_idx = j
                            if drops > 1:
                                break
                    
                    if drops > 1:
                        valid = False
                        break
                    elif drops == 0:
                        if chunk != sorted_chunk:
                            valid = False
                            break
                    else:
                        if (chunk[drop_idx + 1:] + chunk[:drop_idx + 1]) != sorted_chunk:
                            valid = False
                            break
                            
                if valid:
                    total_sum += k
                    
        return total_sum