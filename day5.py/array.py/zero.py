def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast],nums[slow] = nums[slow],nums[fast]
            slow += 1
    
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print("updated array:",nums)

