class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if one rectangle is to the left, right, above, or below the other
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[0] >= rec2[2] or  # right
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[1] >= rec2[3])    # top