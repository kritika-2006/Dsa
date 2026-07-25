def contiguous_array(nums):
    sum_map = {0:-1}
    current_sum= 0
    max_len = 0

    for i ,  num in enumerate(nums):
    
        if num == 1:
           current_sum += 1
        else:
            current_sum -= 1

        if current_sum in sum_map:
            # First index se abhi ki index tak ki length nikalo
            length = i - sum_map[current_sum]
            max_len = max(max_len, length)
        else:
            # Pehli baar sum mila toh index save kar lo
            sum_map[current_sum] = i
    return max_len
nums = [0,1,0,1,1,1,0]
print("max length:",contiguous_array(nums))