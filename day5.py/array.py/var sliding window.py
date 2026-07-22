def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = 999999
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            current_length = right - left + 1
            
            if current_length < min_length:
                min_length = current_length
            
            current_sum -= nums[left]
            left += 1  # <-- YEH WALA ADD KARO (Line 18)
            
    return min_length  # <-- YEH FOR LOOP KE BAHAR HOGA

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))