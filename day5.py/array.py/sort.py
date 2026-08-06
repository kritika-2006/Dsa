def sort(nums):
    n = len(nums)

    for i in range(0,n-1):
        if nums[i] > nums[i+1]: # nums[i] big h mtlb sort nhi hua 
            return False
    return True
nums = [1,2,4,89]
print("sorted array:",sort(nums))