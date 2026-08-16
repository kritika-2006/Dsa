def max_consecutive(nums,k):
    zeros = 0
    left = 0
    right = 0
    maxi = 0
    n = len(nums)

    while right < n:
        if nums[right] == 0:
            zeros += 1
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        if zeros <= k:
            maxi = max(maxi,right-left+1)
        right += 1
    return maxi
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print("max length:",max_consecutive(nums,k))