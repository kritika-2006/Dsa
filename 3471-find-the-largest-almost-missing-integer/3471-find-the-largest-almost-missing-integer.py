class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k == 1
        if k == 1:
            count = Counter(nums)
            ans = -1
            for num, freq in count.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
        
        # Case 2: k == n
        if k == n:
            return max(nums)
        
        # Case 3: 1 < k < n
        first = nums[0]
        last = nums[-1]
        count = Counter(nums)
        
        ans = -1
        if count[first] == 1:
            ans = max(ans, first)
        if count[last] == 1:
            ans = max(ans, last)
            
        return ans