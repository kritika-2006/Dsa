def sliding_window(nums,k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range (k,len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k 
nums = [1,12,-5,-6,50,3]
k = 4
print("Average of max:",sliding_window(nums,k))