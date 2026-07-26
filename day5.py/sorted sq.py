def sorted(nums):
    left = 0
    right = len(nums) - 1
    res = [0] * len(nums)
    pos = len(nums) - 1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            res[pos] = left_sq
            left += 1
        else:
            res[pos] = right_sq
            right -= 1
            
        pos -= 1  # Next position piche khiskao
        
    return res

# Test Case
nums = [-4, -1, 0, 3, 10]
print("Square of the result:", sorted(nums))