def sorted(nums,target):
    left = 0
    right = len(nums) - 1
    current_sum = 0

    while left < right :
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1] 
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return current_sum 
nums = [2,3,4]
target = 6
print("sum of the indexes:", sorted(nums,target))
