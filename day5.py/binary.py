def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = len(arr) - 1
    
    return -1

my_list = [10,20,30,40,50,60,70]
print(binary_search(my_list,60))

