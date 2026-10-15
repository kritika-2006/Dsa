class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Outer loop for starting index of subarray
        for i in range(n):
            seen = set()
            # Inner loop for ending index of subarray
            for j in range(i, n):
                seen.add(nums[j])
                # Distinct count for current subarray is the size of the set
                distinct_count = len(seen)
                # Add the square of the distinct count to total sum
                total_sum += distinct_count ** 2
                
        return total_sum