class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make sure low is the smaller index and high is the larger index
        low, high = min(min_idx, max_idx), max(min_idx, max_idx)

        # Option 1: Remove both elements from the left front
        del_left = high + 1

        # Option 2: Remove both elements from the right back
        del_right = n - low

        # Option 3: Remove low from left and high from right
        del_both = (low + 1) + (n - high)

        return min(del_left, del_right, del_both)