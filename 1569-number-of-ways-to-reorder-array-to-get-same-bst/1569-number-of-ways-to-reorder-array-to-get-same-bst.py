import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            # Split elements into left and right subtrees
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Number of ways to form left and right subtrees recursively
            ways_left = helper(left)
            ways_right = helper(right)
            
            # Combinations: ways to interleave left and right elements
            # math.comb(L + R, L)
            comb = math.comb(len(left) + len(right), len(left))
            
            return (comb * ways_left * ways_right) % MOD

        # Subtract 1 because the question asks for ways to *reorder* (excluding the original array)
        return (helper(nums) - 1 + MOD) % MOD