def maxaverage_subarray(nums,k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range (k,len(nums)):
        # new element add on 
        current_sum += nums[i]
        # purana element remove
        current_sum -= nums[i-k]
        # update max_sum
        max_sum = max(max_sum,current_sum)
    return max_sum / k 
nums = [1, 12, -5, -6, 50, 3]
k = 4
print("max average of the sum :",maxaverage_subarray(nums,k))
         