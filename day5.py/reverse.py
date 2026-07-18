def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left = left + 1
        right = right - 1
    return arr

my_list = [10,20,30,40,50]
print(reverse_array(my_list))