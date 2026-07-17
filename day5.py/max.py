def find_max(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]  
    return max_num
my_list = [12,45,2,78,30]
print(find_max(my_list))