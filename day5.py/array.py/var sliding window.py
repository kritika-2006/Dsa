def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf') # Infinity se start karte hain taaki min comparison sahi ho

# 'right' pointer pooray array par chalega (EXPAND)
    for right in range(len(nums)):
        current_sum += nums[right]
# Jab tak target meet ho raha hai, tab tak left ko aage badhao (SHRINK)
        while current_sum >= target:
            # Window ki length update karo
            current_len = right - left + 1
            min_length = min(min_length, current_len)
            # Left element ko remove karo aur left pointer aage badhao
            current_sum -= nums[left]
            left += 1
            # Agar min_len change hi nahi hua (target kabhi nahi mila), toh 0 return karo
    return min_length if min_length!= float('inf') else 0
nums = [2, 3, 1, 2, 4, 3]
target = 7
print("min len:",min_subarray_len(target,nums))