def two_sum(nums,target):
    left = 0
    right = len(nums) - 1
    current_sum = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return[left,right]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    
nums = [2,7,11,15]
target = 13
print("sum of index:",two_sum(nums,target))