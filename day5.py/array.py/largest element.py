def largest_element(nums):
    largest = 0
    n = len(nums)

    for i in range(0,n):
        if nums[i] > largest:
            largest = nums[i]
    return largest
nums = [3,7,8,11]
print("largest:",largest_element(nums))
