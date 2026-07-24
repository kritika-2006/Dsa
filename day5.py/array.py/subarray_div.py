def subarray_div(nums,k):
    remainder_counts = {0:1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        rem = current_sum % k

        if rem in remainder_counts:
            count += remainder_counts[rem]
        remainder_counts[rem] = remainder_counts.get(rem , 0) +1
    return count
nums = [4,5,0,-2,-3,1]
k = 5
print("Total subarrays is divisible by k:",subarray_div(nums,k))
