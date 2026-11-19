class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # 3 ways to remove 2 elements from the extremes:
        # 1. Remove two smallest: nums[n-1] - nums[2]
        # 2. Remove two largest: nums[n-3] - nums[0]
        # 3. Remove one smallest and one largest: nums[n-2] - nums[1]
        return min(
            nums[n - 1] - nums[2],
            nums[n - 3] - nums[0],
            nums[n - 2] - nums[1]
        )

    # Alias for platform method name compatibility
    solve = minimizeSum