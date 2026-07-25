def two_input(nums,target):
    left = 0
    right = len(nums) - 1
# two pointer vala ma always while loop 
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
    
nums = [2,7,11,15]
target = 9
print("sum:",two_input(nums,target))

        

