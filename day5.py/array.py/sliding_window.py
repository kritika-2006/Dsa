def sliding_window(nums,k):
    current_sum  = sum(nums[:k])
    max_sum = current_sum
    n = len(nums)
    for i in range(k,n):
        if i >= k :
           current_sum = current_sum + nums[i] - nums[i - k]
           max_sum = max(max_sum , current_sum)
    return max_sum 
nums = [2, 1, 5, 1, 3, 2]   
k = 3
print("sum:",sliding_window(nums,k))  

