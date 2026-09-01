from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        # Step 1: Sort numbers along with their original indices
        sorted_nums = sorted(nums)
        
        # Step 2: Group connected components where abs(a - b) <= limit
        groups = []
        val_to_group = {}
        
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append(deque([num]))
            else:
                groups[-1].append(num)
            
            # Map number to its group index
            val_to_group[num] = len(groups) - 1
            
        # Step 3: Reconstruct the result array by popping smallest elements from each group
        result = []
        for num in nums:
            group_idx = val_to_group[num]
            result.append(groups[group_idx].popleft())
            
        return result