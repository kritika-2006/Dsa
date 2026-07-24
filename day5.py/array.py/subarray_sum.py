def subarray_sum(nums,k):
    prefix_counts = {0:1}
    current_sum = 0
    count = 0

    for num in nums: 
        # current sum update
        current_sum += num
        # target 
        target = current_sum - k
        # Agar target hashmap mein hai, toh uska count result mein add karo
        if target in prefix_counts:
            count += prefix_counts[target]
            # Current sum ko hashmap mein store/update karo
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0)+1
             
    return count
nums = [1,1,1]
k = 2
print("Total Subarrays:", subarray_sum(nums,k))

