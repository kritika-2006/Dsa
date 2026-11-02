class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)

    # Aliases for platform method compatibility
    minMovesII = minMoves2
    minimumMoves = minMoves2
    solve = minMoves2