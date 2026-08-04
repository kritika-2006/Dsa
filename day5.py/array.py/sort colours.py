def sort_colours(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # 0 ko low par bhej do
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 apni jagah sahi hai, bas mid aage badhao
            mid += 1
        elif nums[mid] == 2:
            # 2 ko high par bhej do
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums  # Output ke liye return zaroori hai!


nums = [2, 0, 2, 1, 1, 0]
print("sort colours:", sort_colours(nums))