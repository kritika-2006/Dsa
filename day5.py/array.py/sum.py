def find_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum = total_sum + arr[i]
    return total_sum
    
my_list = [3,4,5,6,7]
print(find_sum(my_list))