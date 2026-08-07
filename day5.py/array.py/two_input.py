def two_sum(nums,target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]
nums = [5,9,1,2,4,15,6,3]
target = 13
print("index of the sum:",two_sum(nums,target))
