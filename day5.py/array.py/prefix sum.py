def make_prefix_sums(nums):
    prefix = [0] * len(nums)
    # ist element same 
    prefix[0] = nums[0]

    # baaki elements ko sum ma add karna h 
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    return prefix
nums = [2,4,1,3,5]
print("Original array:",nums)
print("Prefix sum array:",make_prefix_sums(nums))