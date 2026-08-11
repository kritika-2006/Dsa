def max_Product_subarray(nums):
    n = len(nums)
    max_so_far = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    for i in range(1,n):
    
        if nums[i] < 0:
           current_max,current_min = current_min,current_max
        current_max = max(nums[i], nums[i] * current_max)
        current_min = min(nums[i],nums[i] * current_min)
        max_so_far = max(max_so_far, current_max)
    return max_so_far
nums = [2,3,-2,4,-1]
print(" max Product:",max_Product_subarray(nums))