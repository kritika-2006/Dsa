class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        return sum(x - min_val for x in nums)

    # Aliases for platform method name compatibility
    minimumMoves = minMoves
    solve = minMoves