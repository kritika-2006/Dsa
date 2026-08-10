def maxsubarray(nums):
    n = len(nums)
    total = 0
    maxi = float("-inf")

    for i in range(0,n):
        total = total + nums[i]
        maxi = max(maxi,total)

        if total < 0:
            total = 0
    return maxi
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("",maxsubarray(nums))