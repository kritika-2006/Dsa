def max_sum_subarray(num,k):
    window_sum = sum(num[:k])
    max_sum = window_sum

    for i in range(len(num) - k):
        window_sum = window_sum - num[i] + num[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum
print(max_sum_subarray([2,1,5,1,3,2],3))