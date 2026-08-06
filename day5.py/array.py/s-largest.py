def s_largest(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    # 1 loop to find out the largest
    for i in range (0,n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]   
        elif nums[i] > s_largest and nums[i] != largest:
             s_largest = nums[i]
    return s_largest

nums = [3,4,54,67]
print("second largest:",s_largest(nums))
