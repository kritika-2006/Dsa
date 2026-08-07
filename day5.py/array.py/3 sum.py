def three_sum(nums):
    result = set()
    n = len(nums)
    for i in range(0,n):
        my_set = set()
        for j in range(i+1,n):
            # k  
            third = -(nums[i] + nums[j])
            if third in my_set:
               temp = sorted([nums[i],nums[j],third])
               result.add(tuple(temp))
            my_set.add(nums[j])
    return [list(ans) for ans in result]
nums = [-4, -1, -1, 0, 1, 2]
print("sum:",three_sum(nums))