class Solution:

  def maxAlternatingSum(self, nums: list[int]) -> int:
    # Saare numbers ke squares nikal kar sort kar lo
    squares = sorted([x * x for x in nums])

    n = len(nums)
    k = n // 2  # Un elements ka count jo subtract honge

    # Pehle k elements subtract honge, baaki add honge
    subtract_sum = sum(squares[:k])
    add_sum = sum(squares[k:])

    return add_sum - subtract_sum