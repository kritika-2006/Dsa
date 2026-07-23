def make_prefix_sum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix

# Range Sum Function
def range_sum(prefix, L , R):
    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L - 1]

nums =[2,4,1,3,5]
prefix = make_prefix_sum(nums)
print("sum from index 1 to 3:",range_sum(prefix, 1 , 3))
print("sum from index 0 to 2:", range_sum(prefix, 0, 2))